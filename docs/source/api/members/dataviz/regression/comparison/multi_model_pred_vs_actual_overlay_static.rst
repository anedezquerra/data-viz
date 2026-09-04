dataviz.regression.comparison.multi_model_pred_vs_actual_overlay_static
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: multi_model_pred_vs_actual_overlay_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.comparison import multi_model_pred_vs_actual_overlay_static

   rng = np.random.default_rng(42)
   y_true = rng.normal(10.0, 2.0, size=60)
   predictions_per_model = [
       y_true + rng.normal(0.0, 0.5, size=60),
       y_true + rng.normal(0.0, 0.8, size=60),
   ]

   ax = multi_model_pred_vs_actual_overlay_static(
       y_true, predictions_per_model, ["OLS", "Ridge"]
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/multi_model_pred_vs_actual_overlay_static.png" alt="multi_model_pred_vs_actual_overlay_static example output"><figcaption>Example output</figcaption></figure></div>
