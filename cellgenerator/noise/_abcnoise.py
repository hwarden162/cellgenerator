from abc import ABC, abstractmethod
import numpy as np

class _ABCNoise():
    
    @abstractmethod
    def _generate_noise(self, img: np.ndarray) -> np.ndarray:
        pass
    
    def _add_noise(self, img: np.ndarray) -> np.ndarray:
        if not isinstance(img, np.ndarray): raise TypeError("img should be a numpy array")
        if img.ndim != 2: raise ValueError("img should be a 2D array")
        noise = self._generate_noise(img)
        return np.clip(img * noise, 0, 1)
