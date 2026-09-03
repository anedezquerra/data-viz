dataviz.xai.comparison.importance_comparison_heatmap_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.comparison</p></div>

.. currentmodule:: dataviz.xai.comparison

.. autofunction:: importance_comparison_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.comparison import importance_comparison_heatmap_static

   importance_matrix = pd.DataFrame(
       {
           "age": [0.30, 0.22, 0.26],
           "income": [0.25, 0.31, 0.28],
           "tenure": [0.10, 0.08, 0.12],
       },
       index=["logistic", "random_forest", "gradient_boosting"],
   )

   ax = importance_comparison_heatmap_static(importance_matrix)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
