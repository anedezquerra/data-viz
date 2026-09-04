dataviz.xai.cohort.shap_cluster_heatmap_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.cohort</p></div>

.. currentmodule:: dataviz.xai.cohort

.. autofunction:: shap_cluster_heatmap_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.cohort import shap_cluster_heatmap_interactive

   rng = np.random.default_rng(7)
   shap_values = rng.normal(0.0, 0.2, size=(48, 5))
   feature_names = ["age", "income", "tenure", "debt", "region_score"]

   fig = shap_cluster_heatmap_interactive(shap_values, feature_names)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/cohort/shap_cluster_heatmap_interactive.png" alt="shap_cluster_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
