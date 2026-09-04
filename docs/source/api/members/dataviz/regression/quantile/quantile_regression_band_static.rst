dataviz.regression.quantile.quantile_regression_band_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: quantile_regression_band_static

Use case
--------

Use to visualize fitted low/median/high quantile curves against the data when modeling more than the conditional mean.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.quantile import quantile_regression_band_static

   rng = np.random.default_rng(42)
   distance_km = pd.Series(rng.uniform(2, 60, 25).round(1), name="distance_km")
   delivery_min = pd.Series(
       8 + 1.6 * distance_km + rng.gamma(2.0, 3.0, 25), name="delivery_min"
   )
   q10 = 6 + 1.45 * distance_km
   q50 = 8 + 1.60 * distance_km
   q90 = 11 + 1.85 * distance_km

   ax = quantile_regression_band_static(
       distance_km, delivery_min, q10, q50, q90,
       title="Courier delivery time: 10/50/90% quantile band",
       color="#2a6f97", band_color="#a8d5e5", theme="minimal",
   )
   ax.set_xlabel("Distance (km)")
   ax.set_ylabel("Delivery time (min)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/quantile/quantile_regression_band_static.png" alt="quantile_regression_band_static example output"><figcaption>Example output</figcaption></figure></div>
