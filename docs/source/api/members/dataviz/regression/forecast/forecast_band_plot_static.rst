dataviz.regression.forecast.forecast_band_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: forecast_band_plot_static

Use case
--------

Use to show the forecast path with its prediction band and check how often actuals fall inside it.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import forecast_band_plot_static

   rng = np.random.default_rng(42)
   days = pd.date_range("2025-03-01", periods=20, freq="D")
   trend = 120.0 + 0.8 * np.arange(20)
   central = pd.Series(trend + rng.normal(0, 1.0, 20), index=days,
                       name="price_forecast")
   actual = pd.Series(trend + rng.normal(0, 3.0, 20), index=days,
                      name="spot_price")
   lower = central - 5.0
   upper = central + 5.0

   ax = forecast_band_plot_static(
       days, actual, central, lower, upper,
       title="Wholesale Coffee Price: Forecast with 90% Band",
       pred_color="#1f77b4", band_color="#aec7e8")
   ax.set_ylabel("Price (USD/kg)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/forecast_band_plot_static.png" alt="forecast_band_plot_static example output"><figcaption>Example output</figcaption></figure></div>
