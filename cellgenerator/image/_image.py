import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as PILImage
from typing import Tuple

from ..mask._abcmask import _AbstractMask
from ..noise._abcnoise import _ABCNoise
from ..noise._const_noise import ConstantNoise
from ..stain._abcstain import _AbstractStain

class Image():
    def __init__(
        self,
        dim: Tuple[int, int],
        mask: _AbstractMask,
        stain: _AbstractStain,
        noise: _ABCNoise = ConstantNoise(),
        stain_min: float = 0.4,
        stain_max: float = 1.0
    ) -> None:
        if not isinstance(dim, tuple): raise TypeError("dim should be a tuple")
        if len(dim) != 2: raise ValueError("dim should have length 2")
        if not all(isinstance(entry, int) for entry in dim): raise TypeError("dim entries should all be integers")
        if not isinstance(mask, _AbstractMask): raise TypeError("mask provided is invalid")
        if not isinstance(stain, _AbstractStain): raise TypeError("stain provided is invalid")
        if not isinstance(noise, _ABCNoise): raise TypeError("noise provided is invalid")
        if isinstance(stain_min, int): stain_min = float(stain_min)
        if not isinstance(stain_min, float): raise TypeError("stain_min should be a float")
        if (stain_min <= 0 ) or (stain_min > 1): raise ValueError("stain_min should be between 0 and 1")
        if isinstance(stain_max, int): stain_max = float(stain_max)
        if not isinstance(stain_max, float): raise TypeError("stain_max should be a float")
        if (stain_max <= 0 ) or (stain_max > 1): raise ValueError("stain_max should be between 0 and 1")
        if stain_min > stain_max: raise ValueError("stain_min should be less than stain_max")
        self._dim = dim
        self._mask = mask._generate_mask(self._dim)
        self._stain = stain._generate_stain(self._dim)
        self._noise = noise
        self._stain_min = stain_min
        self._stain_max = stain_max
        
    def get_img(self, dim: Tuple[int, int], rotate: float = 0.0) -> PILImage:
        if not isinstance(dim, tuple): raise TypeError("dim should be a tuple")
        if len(dim) != 2: raise ValueError("dim should have length 2")
        if not all(isinstance(entry, int) for entry in dim): raise TypeError("dim entries should all be integers")
        if isinstance(rotate, int): rotate = float(rotate)
        if not isinstance(rotate, float): raise TypeError("rotate should be a float")
        mask = self._mask
        stain = self._stain
        stain -= stain.min()
        stain /= stain.max()
        stain *= (self._stain_max - self._stain_min)
        stain += self._stain_min
        img = mask * stain
        img = self._noise._add_noise(img)
        img *= 255
        img = img.astype(np.uint8)
        img = PILImage.fromarray(img, mode="L")
        img = img.rotate(rotate)
        img = img.resize(dim)
        return img
    
    def plot(self, dim: Tuple[int, int], rotate: float = 0.0) -> None:
        if not isinstance(dim, tuple): raise TypeError("dim should be a tuple")
        if len(dim) != 2: raise ValueError("dim should have length 2")
        if not all(isinstance(entry, int) for entry in dim): raise TypeError("dim entries should all be integers")
        if isinstance(rotate, int): rotate = float(rotate)
        if not isinstance(rotate, float): raise TypeError("rotate should be a float")
        img = self.get_img(dim, rotate)
        img = np.array(img)
        plt.imshow(img, cmap="grey")
        plt.axis('off')
        plt.show()
    
    def save(self, path: str, dim: Tuple[int, int], rotate: float = 0.0) -> None:
        if not isinstance(path, str): raise ValueError("path should be a string")
        if not isinstance(dim, tuple): raise TypeError("dim should be a tuple")
        if len(dim) != 2: raise ValueError("dim should have length 2")
        if not all(isinstance(entry, int) for entry in dim): raise TypeError("dim entries should all be integers")
        if isinstance(rotate, int): rotate = float(rotate)
        if not isinstance(rotate, float): raise TypeError("rotate should be a float")
        img = self.get_img(dim, rotate)
        img.save(path, "PNG")