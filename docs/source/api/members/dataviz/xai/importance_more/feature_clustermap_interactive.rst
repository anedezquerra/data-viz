dataviz.xai.importance_more.feature_clustermap_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: feature_clustermap_interactive

Use case
--------

Use to group features that share an importance signature across models or folds, revealing redundant or cohort-specific signals.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.importance_more import feature_clustermap_interactive

   importance_matrix = pd.DataFrame(
       {
           "logistic": [0.30, 0.25, 0.10, 0.05],
           "random_forest": [0.22, 0.31, 0.08, 0.12],
           "xgboost": [0.26, 0.28, 0.12, 0.09],
       },
       index=["age", "income", "tenure", "debt"],
   )

   fig = feature_clustermap_interactive(importance_matrix)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_more/feature_clustermap_interactive.png" alt="feature_clustermap_interactive example output"><figcaption>Example output</figcaption></figure></div>
