dataviz.xai.shap_extra.shap_interaction_heatmap_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_interaction_heatmap_interactive

Use case
--------

Use to find which feature pairs carry the strongest SHAP interaction effects before drilling into dependence plots.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.shap_extra import shap_interaction_heatmap_interactive

   importances = np.array([0.42, 0.31, 0.18])
   feature_names = ["age", "income", "tenure"]
   shap_values = np.array([[0.1, -0.2, 0.3], [0.2, -0.1, 0.1]])
   feature_values = np.array([0, 1, 2, 3])
   pd_values = np.array([0.2, 0.25, 0.31, 0.34])

   fig = shap_interaction_heatmap_interactive(shap_values, feature_names)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_extra/shap_interaction_heatmap_interactive.png" alt="shap_interaction_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
