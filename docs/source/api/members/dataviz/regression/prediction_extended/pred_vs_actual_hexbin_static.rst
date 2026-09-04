dataviz.regression.prediction_extended.pred_vs_actual_hexbin_static
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction_extended</p></div>

.. currentmodule:: dataviz.regression.prediction_extended

.. autofunction:: pred_vs_actual_hexbin_static

Use case
--------

Use when many points overplot a predicted-vs-actual scatter; the hexbin density reveals where predictions concentrate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.prediction_extended import pred_vs_actual_hexbin_static

   rng = np.random.default_rng(42)
   batches = pd.Series(np.arange(1, 121), name="batch")
   actual_yield = pd.Series(
       rng.gamma(shape=9.0, scale=4.0, size=120), name="actual_yield_kg"
   )
   predicted_yield = pd.Series(
       0.85 * actual_yield + 5.0 + rng.normal(0, 3.5, 120), name="predicted_yield_kg"
   )

   ax = pred_vs_actual_hexbin_static(
       actual_yield, predicted_yield, gridsize=18,
       title="Chemical batch yield: predicted vs actual density",
       cmap="cividis", theme="minimal",
   )
   ax.set_xlabel("Actual yield (kg)")
   ax.set_ylabel("Predicted yield (kg)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction_extended/pred_vs_actual_hexbin_static.png" alt="pred_vs_actual_hexbin_static example output"><figcaption>Example output</figcaption></figure></div>
