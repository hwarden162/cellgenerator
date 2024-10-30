from abc import ABC, abstractmethod
import numpy as np
from typing import Tuple

class _AbstractStain(ABC):
    @abstractmethod
    def _generate_stain(self, dim: Tuple[int,int]) -> np.ndarray:
        pass