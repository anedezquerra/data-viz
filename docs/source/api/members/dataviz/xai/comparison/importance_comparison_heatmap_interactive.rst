dataviz.xai.comparison.importance_comparison_heatmap_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.comparison</p></div>

.. currentmodule:: dataviz.xai.comparison

.. autofunction:: importance_comparison_heatmap_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.comparison import importance_comparison_heatmap_interactive

   importance_matrix = pd.DataFrame(
       {
           "age": [0.30, 0.22, 0.26],
           "income": [0.25, 0.31, 0.28],
           "tenure": [0.10, 0.08, 0.12],
       },
       index=["logistic", "random_forest", "gradient_boosting"],
   )

   fig = importance_comparison_heatmap_interactive(importance_matrix)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/comparison/importance_comparison_heatmap_interactive.png" alt="importance_comparison_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
