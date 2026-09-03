dataviz.xai.importance_more.importance_correlation_heatmap_interactive
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: importance_correlation_heatmap_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.importance_more import importance_correlation_heatmap_interactive

   importances_by_model = pd.DataFrame(
       {
           "logistic": [0.30, 0.25, 0.10],
           "random_forest": [0.22, 0.31, 0.08],
           "xgboost": [0.26, 0.28, 0.12],
       },
       index=["age", "income", "tenure"],
   )

   fig = importance_correlation_heatmap_interactive(importances_by_model)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
