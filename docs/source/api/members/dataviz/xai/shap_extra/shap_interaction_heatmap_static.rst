dataviz.xai.shap_extra.shap_interaction_heatmap_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_interaction_heatmap_static

Use case
--------

Use to find which feature pairs carry the strongest SHAP interaction effects before drilling into dependence plots.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_extra import shap_interaction_heatmap_static

   interaction_matrix = np.array(
       [
           [0.20, 0.05, 0.02, 0.01],
           [0.05, 0.30, 0.04, 0.02],
           [0.02, 0.04, 0.15, 0.03],
           [0.01, 0.02, 0.03, 0.10],
       ]
   )
   feature_names = ["age", "income", "tenure", "debt"]

   ax = shap_interaction_heatmap_static(interaction_matrix, feature_names)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_extra/shap_interaction_heatmap_static.png" alt="shap_interaction_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
