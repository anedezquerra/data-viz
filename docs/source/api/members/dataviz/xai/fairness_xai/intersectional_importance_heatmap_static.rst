dataviz.xai.fairness_xai.intersectional_importance_heatmap_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.fairness_xai</p></div>

.. currentmodule:: dataviz.xai.fairness_xai

.. autofunction:: intersectional_importance_heatmap_static

Use case
--------

Use to audit feature importance across intersectional segments, e.g. gender by age group, in one heatmap.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.fairness_xai import intersectional_importance_heatmap_static

   features = [
       "credit_score", "debt_to_income", "utilization", "annual_income", "loan_amount",
   ]
   importance_cube = pd.DataFrame(
       {
           "urban|high_income": [0.34, 0.20, 0.16, 0.12, 0.10],
           "urban|low_income": [0.26, 0.28, 0.21, 0.09, 0.13],
           "rural|high_income": [0.30, 0.22, 0.15, 0.15, 0.11],
           "rural|low_income": [0.18, 0.31, 0.24, 0.08, 0.16],
       },
       index=features,
   )

   ax = intersectional_importance_heatmap_static(
       importance_cube,
       title="Importance by Intersectional Segment (Region x Income Band)",
       cmap="cividis",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/fairness_xai/intersectional_importance_heatmap_static.png" alt="intersectional_importance_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
