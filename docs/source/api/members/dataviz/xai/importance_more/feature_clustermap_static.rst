dataviz.xai.importance_more.feature_clustermap_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: feature_clustermap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.importance_more import feature_clustermap_static

   importance_matrix = pd.DataFrame(
       {
           "logistic": [0.30, 0.25, 0.10, 0.05],
           "random_forest": [0.22, 0.31, 0.08, 0.12],
           "xgboost": [0.26, 0.28, 0.12, 0.09],
       },
       index=["age", "income", "tenure", "debt"],
   )

   ax = feature_clustermap_static(importance_matrix)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
