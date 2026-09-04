dataviz.regression.spatial.spatial_residual_map_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.spatial</p></div>

.. currentmodule:: dataviz.regression.spatial

.. autofunction:: spatial_residual_map_static

Use case
--------

Use to map regression residuals by longitude and latitude to reveal geographic clusters of over- or under-prediction the model missed.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.spatial import spatial_residual_map_static

   rng = np.random.default_rng(42)
   n = 45
   lon = -104.99 + rng.uniform(-0.25, 0.25, n)   # Denver metro
   lat = 39.74 + rng.uniform(-0.20, 0.20, n)
   true_price = 320 + 180 * (lat - 39.74) + rng.normal(0, 25, n)
   pred_price = 320 + 90 * (lat - 39.74)          # underfits the north-south gradient
   residuals = true_price - pred_price

   ax = spatial_residual_map_static(
       lon, lat, residuals, cmap="coolwarm",
       title="Denver housing model: geographic residual map (k$)",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/spatial/spatial_residual_map_static.png" alt="spatial_residual_map_static example output"><figcaption>Example output</figcaption></figure></div>
