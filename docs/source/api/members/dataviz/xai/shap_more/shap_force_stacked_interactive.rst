dataviz.xai.shap_more.shap_force_stacked_interactive
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_force_stacked_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.shap_more import shap_force_stacked_interactive

   rng = np.random.default_rng(43)
   shap_values = rng.normal(0.0, 0.15, size=(6, 4))
   feature_names = ["age", "income", "tenure", "debt"]

   fig = shap_force_stacked_interactive(shap_values, base_value=0.5, feature_names=feature_names)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_force_stacked_interactive.png" alt="shap_force_stacked_interactive example output"><figcaption>Example output</figcaption></figure></div>
