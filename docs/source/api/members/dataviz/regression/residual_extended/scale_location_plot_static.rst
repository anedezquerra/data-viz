dataviz.regression.residual_extended.scale_location_plot_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: scale_location_plot_static

Use case
--------

Use to check homoscedasticity by plotting sqrt of absolute standardized residuals against fitted values.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_extended import scale_location_plot_static

   rng = np.random.default_rng(42)
   orders = pd.Series(np.arange(1, 46), name="order")
   actual_cost = pd.Series(
       rng.uniform(20, 400, 45).round(1), name="actual_cost_usd"
   )
   hetero_noise = rng.normal(0, 1, 45) * (4 + 0.05 * actual_cost)
   predicted_cost = pd.Series(actual_cost + hetero_noise, name="predicted_cost_usd")

   ax = scale_location_plot_static(
       actual_cost, predicted_cost,
       title="Shipping cost model: scale-location check",
       color="#4878d0", trend_color="#d62728", theme="minimal",
   )
   ax.set_xlabel("Predicted cost (USD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/scale_location_plot_static.png" alt="scale_location_plot_static example output"><figcaption>Example output</figcaption></figure></div>
