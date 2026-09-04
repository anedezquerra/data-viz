dataviz.regression.quantile.quantile_loss_curve_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: quantile_loss_curve_static

Use case
--------

Use to compare pinball loss across quantile levels when selecting or evaluating quantile-regression models.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.quantile import quantile_loss_curve_static

   rng = np.random.default_rng(42)
   quantiles = pd.Series(np.round(np.arange(0.05, 0.96, 0.05), 2), name="tau")
   residual_sample = rng.normal(0, 2.5, 400)
   losses = pd.Series(
       [np.mean(np.maximum(t * residual_sample, (t - 1) * residual_sample))
        for t in quantiles],
       name="pinball_loss",
   )

   ax = quantile_loss_curve_static(
       quantiles, losses,
       title="Demand forecasting: pinball loss by quantile level",
       color="#6a4c93", theme="minimal",
   )
   ax.set_xlabel("Quantile level (tau)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/quantile/quantile_loss_curve_static.png" alt="quantile_loss_curve_static example output"><figcaption>Example output</figcaption></figure></div>
