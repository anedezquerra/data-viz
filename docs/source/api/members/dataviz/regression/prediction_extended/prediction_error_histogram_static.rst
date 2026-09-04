dataviz.regression.prediction_extended.prediction_error_histogram_static
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction_extended</p></div>

.. currentmodule:: dataviz.regression.prediction_extended

.. autofunction:: prediction_error_histogram_static

Use case
--------

Use to inspect the distribution of prediction errors for bias, skew, or heavy tails, optionally cumulatively.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.prediction_extended import prediction_error_histogram_static

   rng = np.random.default_rng(42)
   months = pd.date_range("2023-01-01", periods=30, freq="MS")
   actual_sales = pd.Series(
       980 + 12 * np.sin(np.arange(30) / 4.8) + rng.normal(0, 40, 30),
       index=months, name="actual_units",
   )
   forecast_sales = pd.Series(
       actual_sales + rng.normal(6, 28, 30), index=months, name="forecast_units"
   )

   ax = prediction_error_histogram_static(
       actual_sales, forecast_sales, bins=14,
       title="Retail sales forecast error distribution",
       color="#4878d0", edgecolor="white", theme="minimal",
   )
   ax.set_xlabel("Error: actual minus forecast (units)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction_extended/prediction_error_histogram_static.png" alt="prediction_error_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
