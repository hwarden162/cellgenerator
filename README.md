# cellgenerator

cellgenerator is a Python package for creating images that can be used as synthetic cells for in silico experiments.

A cellgenerator image contains 3 major constituent parts: (1) A mask defining where the object is in the image (2) A stain object defining how the stain will change across the object (3) noise to be added to the image. These cells should be generated at a high resolution and can then be rotated, resized, viewed and saved.

```python
from cellgenerator import Image
from cellgenerator.mask import EllipseMask
from cellgenerator.stain import SpatialStain

em = EllipseMask(200, 400)
ss = SpatialStain(20, 20)
img = Image((1000, 1000), em, ss)
img.plot((80, 80), rotate=35)
```