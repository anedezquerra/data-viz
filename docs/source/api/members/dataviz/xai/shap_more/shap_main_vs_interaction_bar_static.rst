dataviz.xai.shap_more.shap_main_vs_interaction_bar_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_main_vs_interaction_bar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_more import shap_main_vs_interaction_bar_static

   rng = np.random.default_rng(45)
   main_effects = rng.normal([0.20, 0.12, 0.05, 0.03], 0.05, size=(50, 4))
   interaction_effects = rng.normal([0.04, 0.06, 0.01, 0.02], 0.02, size=(50, 4))
   feature_names = ["age", "income", "tenure", "debt"]

   ax = shap_main_vs_interaction_bar_static(
       main_effects, interaction_effects, feature_names,
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_main_vs_interaction_bar_static.png" alt="shap_main_vs_interaction_bar_static example output"><figcaption>Example output</figcaption></figure></div>
