dataviz.xai.comparison.shap_model_agreement_scatter_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.comparison</p></div>

.. currentmodule:: dataviz.xai.comparison

.. autofunction:: shap_model_agreement_scatter_static

Use case
--------

Check whether two models attribute predictions to the same features per instance, quantified by Pearson r.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.comparison import shap_model_agreement_scatter_static

   rng = np.random.default_rng(11)
   shap_a = rng.normal(0.0, 0.3, size=(60, 4))
   shap_b = shap_a + rng.normal(0.0, 0.05, size=(60, 4))
   feature_names = ["age", "income", "tenure", "debt"]

   ax = shap_model_agreement_scatter_static(
       shap_a, shap_b, model_a="random forest", model_b="xgboost",
       feature_names=feature_names,
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/comparison/shap_model_agreement_scatter_static.png" alt="shap_model_agreement_scatter_static example output"><figcaption>Example output</figcaption></figure></div>
