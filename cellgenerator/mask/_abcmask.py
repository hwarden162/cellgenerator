from abc import ABC, abstractmethod
import numpy as np
from typing import Tuple

class _AbstractMask(ABC):
    @abstractmethod
    def _generate_mask(self, dim: Tuple[int, int]) -> np.ndarray:
        pass
