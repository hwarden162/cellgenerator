import numpy as np

from ._abcnoise import _ABCNoise

class ConstantNoise(_ABCNoise):
    def _generate_noise(self, img: np.ndarray) -> np.ndarray:
        if not isinstance(img, np.ndarray): raise TypeError("img should be a numpy array")
        if img.ndim != 2: raise ValueError("img should be a 2D array")
        return np.ones_like(img)