dataviz.xai.cohort.shap_cluster_heatmap_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.cohort</p></div>

.. currentmodule:: dataviz.xai.cohort

.. autofunction:: shap_cluster_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.cohort import shap_cluster_heatmap_static

   rng = np.random.default_rng(7)
   shap_values = rng.normal(0.0, 0.2, size=(48, 5))
   feature_names = ["age", "income", "tenure", "debt", "region_score"]

   ax = shap_cluster_heatmap_static(shap_values, feature_names)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/cohort/shap_cluster_heatmap_static.png" alt="shap_cluster_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
