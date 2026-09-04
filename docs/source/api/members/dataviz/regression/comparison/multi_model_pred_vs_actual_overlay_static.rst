dataviz.regression.comparison.multi_model_pred_vs_actual_overlay_static
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: multi_model_pred_vs_actual_overlay_static

Use case
--------

Use to overlay predicted-vs-actual scatters from several models and spot which one tracks the diagonal most tightly.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.comparison import multi_model_pred_vs_actual_overlay_static

   rng = np.random.default_rng(42)
   actual = pd.Series(rng.uniform(40, 160, 30), name="actual_throughput")
   preds = [actual + rng.normal(0, 6, 30),
            actual * rng.normal(1.0, 0.09, 30),
            actual + rng.normal(4, 10, 30)]
   labels = ["Linear", "Random Forest", "Gradient Boosting"]

   ax = multi_model_pred_vs_actual_overlay_static(
       actual, preds, labels,
       title="Line Throughput: Predicted vs Actual by Model",
       cmap="Dark2")
   ax.set_xlabel("Actual units/hour")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/multi_model_pred_vs_actual_overlay_static.png" alt="multi_model_pred_vs_actual_overlay_static example output"><figcaption>Example output</figcaption></figure></div>
