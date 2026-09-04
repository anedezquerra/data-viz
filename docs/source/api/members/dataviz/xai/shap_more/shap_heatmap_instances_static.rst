dataviz.xai.shap_more.shap_heatmap_instances_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_heatmap_instances_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_more import shap_heatmap_instances_static

   importances = np.array([0.42, 0.31, 0.18])
   feature_names = ["age", "income", "tenure"]
   shap_values = np.array([[0.1, -0.2, 0.3], [0.2, -0.1, 0.1]])
   feature_values = np.array([0, 1, 2, 3])
   pd_values = np.array([0.2, 0.25, 0.31, 0.34])

   ax = shap_heatmap_instances_static(shap_values, feature_names)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_heatmap_instances_static.png" alt="shap_heatmap_instances_static example output"><figcaption>Example output</figcaption></figure></div>
