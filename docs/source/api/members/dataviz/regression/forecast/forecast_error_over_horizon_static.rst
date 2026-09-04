dataviz.regression.forecast.forecast_error_over_horizon_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: forecast_error_over_horizon_static

Use case
--------

Use to see how an error metric such as MAE or RMSE grows as the forecast horizon lengthens.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import forecast_error_over_horizon_static

   rng = np.random.default_rng(42)
   horizons = np.arange(1, 15)
   rmse_by_horizon = pd.Series(1.8 + 0.35 * horizons + rng.normal(0, 0.15, 14),
                               index=horizons, name="rmse_celsius")

   ax = forecast_error_over_horizon_static(
       horizons, rmse_by_horizon,
       title="Cold-Chain Temperature Forecast: RMSE by Horizon",
       color="#2ca02c")
   ax.set_ylabel("RMSE (deg C)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/forecast_error_over_horizon_static.png" alt="forecast_error_over_horizon_static example output"><figcaption>Example output</figcaption></figure></div>
