dataviz.regression.spatial.spatial_residual_map_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.spatial</p></div>

.. currentmodule:: dataviz.regression.spatial

.. autofunction:: spatial_residual_map_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.spatial import spatial_residual_map_static

   rng = np.random.default_rng(42)
   longitudes = rng.uniform(-5.0, 5.0, size=60)
   latitudes = rng.uniform(40.0, 50.0, size=60)
   residuals = rng.normal(0.0, 0.7, size=60)

   ax = spatial_residual_map_static(longitudes, latitudes, residuals)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/spatial/spatial_residual_map_static.png" alt="spatial_residual_map_static example output"><figcaption>Example output</figcaption></figure></div>
