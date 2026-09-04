dataviz.xai.shap_more.shap_beeswarm_plot_interactive
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_beeswarm_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.shap_more import shap_beeswarm_plot_interactive

   rng = np.random.default_rng(41)
   shap_values = rng.normal(0.0, 0.2, size=(80, 4))
   feature_values = rng.normal(0.0, 1.0, size=(80, 4))
   feature_names = ["age", "income", "tenure", "debt"]

   fig = shap_beeswarm_plot_interactive(shap_values, feature_values, feature_names)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_beeswarm_plot_interactive.png" alt="shap_beeswarm_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
