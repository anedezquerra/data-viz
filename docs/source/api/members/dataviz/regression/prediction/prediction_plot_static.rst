dataviz.regression.prediction.prediction_plot_static
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction</p></div>

.. currentmodule:: dataviz.regression.prediction

.. autofunction:: prediction_plot_static

Use case
--------

Use to compare predicted against actual values with a perfect-preference reference line for a quick fit-quality check.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.prediction import prediction_plot_static

   rng = np.random.default_rng(42)
   days = pd.date_range("2025-01-05", periods=24, freq="W")
   actual_demand = pd.Series(
       420 + 3.5 * np.arange(24) + rng.normal(0, 25, 24),
       index=days, name="actual_mwh",
   )
   predicted_demand = pd.Series(
       actual_demand + rng.normal(0, 18, 24), index=days, name="forecast_mwh"
   )

   ax = prediction_plot_static(
       actual_demand, predicted_demand,
       title="Weekly energy demand: forecast vs actual",
       color="#2a6f97", marker_size=60, alpha=0.75,
       line_color="#d62728", theme="minimal",
   )
   ax.set_xlabel("Actual demand (MWh)")
   ax.set_ylabel("Forecast demand (MWh)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction/prediction_plot_static.png" alt="prediction_plot_static example output"><figcaption>Example output</figcaption></figure></div>
