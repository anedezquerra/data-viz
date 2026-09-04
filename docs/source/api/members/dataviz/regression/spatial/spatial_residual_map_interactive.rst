dataviz.regression.spatial.spatial_residual_map_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.spatial</p></div>

.. currentmodule:: dataviz.regression.spatial

.. autofunction:: spatial_residual_map_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.spatial import spatial_residual_map_interactive

   rng = np.random.default_rng(42)
   longitudes = rng.uniform(-5.0, 5.0, size=60)
   latitudes = rng.uniform(40.0, 50.0, size=60)
   residuals = rng.normal(0.0, 0.7, size=60)

   fig = spatial_residual_map_interactive(longitudes, latitudes, residuals)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/spatial/spatial_residual_map_interactive.png" alt="spatial_residual_map_interactive example output"><figcaption>Example output</figcaption></figure></div>
