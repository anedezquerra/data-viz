dataviz.xai.cohort.shap_cluster_heatmap_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.cohort</p></div>

.. currentmodule:: dataviz.xai.cohort

.. autofunction:: shap_cluster_heatmap_static

Use case
--------

Use to discover groups of instances with similar SHAP explanation patterns via clustered heatmap ordering.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.cohort import shap_cluster_heatmap_static

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "utilization",
       "annual_income", "loan_amount", "account_age",
   ]
   prototypes = np.array([
       [0.9, -0.4, 0.3, 0.1, -0.2, 0.0],
       [-0.6, 0.8, -0.5, 0.2, 0.1, -0.1],
       [0.2, -0.2, 0.7, -0.5, 0.4, 0.2],
       [-0.3, 0.1, -0.2, 0.6, -0.3, 0.5],
   ])
   shap_values = np.vstack(
       [p + rng.normal(0, 0.08, size=(20, len(features))) for p in prototypes]
   )

   ax = shap_cluster_heatmap_static(
       shap_values,
       features,
       n_clusters=4,
       title="SHAP Signature Clusters - Credit Applicants",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/cohort/shap_cluster_heatmap_static.png" alt="shap_cluster_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
