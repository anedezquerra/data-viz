dataviz.regression.residual.residual_plot_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual</p></div>

.. currentmodule:: dataviz.regression.residual

.. autofunction:: residual_plot_static

Use case
--------

Use as the first residual diagnostic: plot residuals vs fitted values to reveal nonlinearity or heteroscedasticity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.residual import residual_plot_static

   rng = np.random.default_rng(42)
   homes = pd.Series(np.arange(1, 23), name="listing")
   actual_price = pd.Series(
       rng.uniform(180, 850, 22).round(0), name="actual_price_kusd"
   )
   predicted_price = pd.Series(
       actual_price + rng.normal(0, 32, 22) + 0.05 * (actual_price - 500),
       name="predicted_price_kusd",
   )

   ax = residual_plot_static(
       actual_price, predicted_price,
       title="Home appraisal model: residual diagnostics",
       color="#2a6f97", marker_size=70, alpha=0.8,
       line_color="#d62728", theme="minimal",
   )
   ax.set_xlabel("Predicted price (kUSD)")
   ax.set_ylabel("Residual (kUSD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual/residual_plot_static.png" alt="residual_plot_static example output"><figcaption>Example output</figcaption></figure></div>
