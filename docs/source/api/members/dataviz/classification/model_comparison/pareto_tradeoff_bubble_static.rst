dataviz.classification.model_comparison.pareto_tradeoff_bubble_static
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: pareto_tradeoff_bubble_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.model_comparison import pareto_tradeoff_bubble_static

   models = {
       "Logistic regression": {"precision": 0.81, "recall": 0.86, "auc": 0.90},
       "Random forest": {"precision": 0.88, "recall": 0.90, "auc": 0.95},
       "Gradient boosting": {"precision": 0.85, "recall": 0.89, "auc": 0.93},
       "k-NN": {"precision": 0.78, "recall": 0.80, "auc": 0.84},
   }

   ax = pareto_tradeoff_bubble_static(models)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/pareto_tradeoff_bubble_static.png" alt="pareto_tradeoff_bubble_static example output"><figcaption>Example output</figcaption></figure></div>
