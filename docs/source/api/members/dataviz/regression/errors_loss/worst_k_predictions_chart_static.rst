dataviz.regression.errors_loss.worst_k_predictions_chart_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.errors_loss</p></div>

.. currentmodule:: dataviz.regression.errors_loss

.. autofunction:: worst_k_predictions_chart_static

Use case
--------

Use to surface the k predictions with the largest absolute error for targeted inspection and debugging.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.errors_loss import worst_k_predictions_chart_static

   rng = np.random.default_rng(42)
   actual = pd.Series(rng.uniform(10, 120, 25), name="actual_los_days")
   predicted = pd.Series(actual + rng.normal(0, 9, 25), name="predicted_los_days")

   ax = worst_k_predictions_chart_static(
       actual, predicted, k=8,
       title="Hospital Stay Model: 8 Worst Predictions",
       color="#c0392b")
   ax.set_ylabel("Absolute error (days)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/errors_loss/worst_k_predictions_chart_static.png" alt="worst_k_predictions_chart_static example output"><figcaption>Example output</figcaption></figure></div>
