dataviz.regression.forecast.forecast_vs_actual_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: forecast_vs_actual_static

Use case
--------

Use to overlay actual and forecast series and spot systematic over- or under-prediction over time.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import forecast_vs_actual_static

   rng = np.random.default_rng(42)
   weeks = pd.date_range("2025-01-06", periods=24, freq="W-MON")
   seasonal = 4.0 * np.sin(2 * np.pi * np.arange(24) / 12.0)
   actual = pd.Series(52.0 + seasonal + rng.normal(0, 1.5, 24), index=weeks,
                      name="weekly_demand_kwh")
   forecast = pd.Series(52.0 + seasonal + rng.normal(0, 0.9, 24), index=weeks,
                        name="arima_forecast")

   ax = forecast_vs_actual_static(weeks, actual, forecast,
                                  title="Plant Energy Demand: ARIMA Forecast vs Actual",
                                  true_color="#1f77b4", pred_color="#d62728")
   ax.set_ylabel("Demand (MWh)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/forecast_vs_actual_static.png" alt="forecast_vs_actual_static example output"><figcaption>Example output</figcaption></figure></div>
