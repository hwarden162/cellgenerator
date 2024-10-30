import numpy as np
from typing import Tuple

from ._abcmask import _AbstractMask

class CircleMask(_AbstractMask):
    def __init__(self, radius: float) -> None:
        if isinstance(radius, int): radius = float(radius)
        if not isinstance(radius, float): raise TypeError("radius should be a float")
        if radius <= 0: raise ValueError("radius should be positive")
        self._radius = radius
        
    def _generate_mask(self, dim: Tuple[int, int]) -> np.ndarray:
        if not isinstance(dim, tuple): raise TypeError("dim should be a tuple")
        if len(dim) != 2: raise ValueError("dim should be of length 2")
        if not all([isinstance(entry, int) for entry in dim]): raise TypeError("All entries of dim should be integers")
        y, x = np.ogrid[:dim[0], :dim[1]]
        center_y, center_x = dim[0] / 2, dim[1] / 2
        distance_from_center = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        mask = distance_from_center <= self._radius
        return mask
