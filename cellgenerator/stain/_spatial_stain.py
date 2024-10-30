import numpy as np
from scipy.ndimage import gaussian_filter
from typing import Tuple

from ._abcstain import _AbstractStain

class SpatialStain(_AbstractStain):
    def __init__(self, y_corr: float, x_corr: float) -> None:
        if isinstance(y_corr, int): y_corr = float(y_corr)
        if not isinstance(y_corr, float): raise TypeError("y_corr should be a float")
        if y_corr <= 0: raise ValueError("y_corr should be positive")
        if isinstance(x_corr, int): x_corr = float(x_corr)
        if not isinstance(x_corr, float): raise TypeError("x_corr should be a float")
        if x_corr <= 0: raise ValueError("x_corr should be positive")
        self._y_corr = y_corr
        self._x_corr = x_corr

    def _generate_stain(self, dim: Tuple[int,int]) -> np.ndarray:
        if not isinstance(dim, tuple): raise TypeError("dim should be a tuple")
        if len(dim) != 2: raise ValueError("dim should be of length 2")
        if not all([isinstance(entry, int) for entry in dim]): raise TypeError("All entries of dim should be integers")
        noise = np.random.normal(loc=0, scale=1, size=dim)
        correlated_noise = gaussian_filter(noise, sigma = (self._y_corr, self._x_corr))
        return correlated_noise        