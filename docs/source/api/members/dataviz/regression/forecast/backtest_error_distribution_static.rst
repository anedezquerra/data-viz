dataviz.regression.forecast.backtest_error_distribution_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: backtest_error_distribution_static

Use case
--------

Use to inspect the distribution of backtest errors for bias, skew, and heavy tails.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import backtest_error_distribution_static

   rng = np.random.default_rng(42)
   backtest_errors = pd.Series(
       rng.normal(0.5, 4.0, 400) + rng.choice([0.0, 6.0], size=400, p=[0.9, 0.1]),
       name="backtest_error_bbl")

   ax = backtest_error_distribution_static(
       backtest_errors,
       title="Oil Production Forecast: Backtest Error Distribution",
       bins=40, color="#17becf")
   ax.set_xlabel("Forecast error (bbl/day)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/backtest_error_distribution_static.png" alt="backtest_error_distribution_static example output"><figcaption>Example output</figcaption></figure></div>
