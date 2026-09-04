dataviz.regression.spatial.moran_scatter_static
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.spatial</p></div>

.. currentmodule:: dataviz.regression.spatial

.. autofunction:: moran_scatter_static

Use case
--------

Use to test for spatial autocorrelation by plotting each standardized value against its spatial lag; the slope approximates Moran's I.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.spatial import moran_scatter_static

   rng = np.random.default_rng(42)
   n = 48  # continental US states
   base = rng.normal(0, 1, n)
   unemployment = 4.5 + 1.2 * base + rng.normal(0, 0.4, n)
   spatial_lag = 4.5 + 1.2 * (0.6 * base + 0.4 * rng.normal(0, 1, n))

   ax = moran_scatter_static(
       unemployment, spatial_lag,
       title="State unemployment: Moran scatter of spatial autocorrelation",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/spatial/moran_scatter_static.png" alt="moran_scatter_static example output"><figcaption>Example output</figcaption></figure></div>
