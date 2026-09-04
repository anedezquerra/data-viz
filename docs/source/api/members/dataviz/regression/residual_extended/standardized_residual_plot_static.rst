dataviz.regression.residual_extended.standardized_residual_plot_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: standardized_residual_plot_static

Use case
--------

Use to flag outlying observations by plotting residuals scaled by their estimated standard deviation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_extended import standardized_residual_plot_static

   rng = np.random.default_rng(42)
   claims = pd.Series(np.arange(1, 33), name="claim")
   actual_payout = pd.Series(
       rng.uniform(2, 95, 32).round(1), name="actual_payout_kusd"
   )
   predicted_payout = pd.Series(
       actual_payout + rng.normal(0, 5, 32), name="predicted_payout_kusd"
   )
   predicted_payout.iloc[7] -= 28  # flagged outlier claim

   ax = standardized_residual_plot_static(
       actual_payout, predicted_payout, bound=2.0,
       title="Insurance payout model: standardized residuals",
       color="#ee854a", theme="minimal",
   )
   ax.set_xlabel("Predicted payout (kUSD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/standardized_residual_plot_static.png" alt="standardized_residual_plot_static example output"><figcaption>Example output</figcaption></figure></div>
