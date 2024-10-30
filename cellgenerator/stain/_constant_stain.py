import numpy as np
from typing import Tuple

from ._abcstain import _AbstractStain

class ConstantStain(_AbstractStain):
    def __init__(self, const: float = 1.0) -> None:
        if isinstance(const, int): const = float(const)
        if not isinstance(const, float): raise TypeError("const must be a float")
        if (const <= 0) or (const > 1): raise ValueError("const must be between 0 and 1")
        self._const = const
    
    def _generate_stain(self, dim: Tuple[int,int]) -> np.ndarray:
        if not isinstance(dim, tuple): raise TypeError("dim should be a tuple")
        if len(dim) != 2: raise ValueError("dim should be of length 2")
        if not all([isinstance(entry, int) for entry in dim]): raise TypeError("All entries of dim should be integers")
        return np.ones(dim) * self._const