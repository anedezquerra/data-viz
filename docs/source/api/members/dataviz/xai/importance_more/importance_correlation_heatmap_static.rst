dataviz.xai.importance_more.importance_correlation_heatmap_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: importance_correlation_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.importance_more import importance_correlation_heatmap_static

   importances_by_model = pd.DataFrame(
       {
           "logistic": [0.30, 0.25, 0.10],
           "random_forest": [0.22, 0.31, 0.08],
           "xgboost": [0.26, 0.28, 0.12],
       },
       index=["age", "income", "tenure"],
   )

   ax = importance_correlation_heatmap_static(importances_by_model)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/importance_more/importance_correlation_heatmap_static.png" alt="importance_correlation_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
