dataviz.regression.prediction_extended.error_by_magnitude_plot_static
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction_extended</p></div>

.. currentmodule:: dataviz.regression.prediction_extended

.. autofunction:: error_by_magnitude_plot_static

Use case
--------

Use to check whether errors grow with the size of the target by binning MAE over quantiles of actual values.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.prediction_extended import error_by_magnitude_plot_static

   rng = np.random.default_rng(42)
   stores = pd.Series([f"Store {s:02d}" for s in range(1, 41)], name="store")
   actual_revenue = pd.Series(
       rng.uniform(50, 900, 40).round(0), name="actual_revenue_kusd"
   )
   predicted_revenue = pd.Series(
       actual_revenue * rng.normal(1.0, 0.08, 40) + rng.normal(0, 15, 40),
       name="predicted_revenue_kusd",
   )

   ax = error_by_magnitude_plot_static(
       actual_revenue, predicted_revenue, n_bins=8,
       title="Store revenue model: MAE by revenue magnitude",
       color="#4878d0", line_color="#d62728", theme="minimal",
   )
   ax.set_xlabel("Actual revenue midpoint (kUSD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction_extended/error_by_magnitude_plot_static.png" alt="error_by_magnitude_plot_static example output"><figcaption>Example output</figcaption></figure></div>
