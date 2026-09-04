dataviz.bivariate.trends.area_between_static
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.trends</p></div>

.. currentmodule:: dataviz.bivariate.trends

.. autofunction:: area_between_static

Use case
--------

Use to highlight the gap between two y-series over a shared x axis, such as forecast bounds or tolerance bands.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.trends import area_between_static

   rng = np.random.default_rng(42)
   month = pd.Series(np.arange(1, 37), name="Month")
   forecast = 100.0 + 1.5 * month + np.cumsum(rng.normal(loc=0.0, scale=0.5, size=36))
   lower = pd.Series(forecast - 8.0, name="Lower bound")
   upper = pd.Series(forecast + 8.0, name="Upper bound")

   ax = area_between_static(
       month,
       lower,
       upper,
       title="Demand Forecast Tolerance Band",
       xlabel="Month",
       ylabel="Demand (units)",
       color="steelblue",
       alpha=0.35,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/trends/area_between_static.png" alt="area_between_static example output"><figcaption>Example output</figcaption></figure></div>
