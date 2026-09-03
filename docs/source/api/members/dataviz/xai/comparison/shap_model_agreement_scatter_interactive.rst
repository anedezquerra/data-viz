dataviz.xai.comparison.shap_model_agreement_scatter_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.comparison</p></div>

.. currentmodule:: dataviz.xai.comparison

.. autofunction:: shap_model_agreement_scatter_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.comparison import shap_model_agreement_scatter_interactive

   rng = np.random.default_rng(11)
   shap_a = rng.normal(0.0, 0.3, size=(60, 4))
   shap_b = shap_a + rng.normal(0.0, 0.05, size=(60, 4))
   feature_names = ["age", "income", "tenure", "debt"]

   fig = shap_model_agreement_scatter_interactive(
       shap_a, shap_b, model_a="random forest", model_b="xgboost",
       feature_names=feature_names,
   )
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
