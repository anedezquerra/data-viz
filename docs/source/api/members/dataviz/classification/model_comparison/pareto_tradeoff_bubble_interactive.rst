dataviz.classification.model_comparison.pareto_tradeoff_bubble_interactive
==========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: pareto_tradeoff_bubble_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.model_comparison import pareto_tradeoff_bubble_interactive

   models = {
       "Logistic regression": {"precision": 0.81, "recall": 0.86, "auc": 0.90},
       "Random forest": {"precision": 0.88, "recall": 0.90, "auc": 0.95},
       "Gradient boosting": {"precision": 0.85, "recall": 0.89, "auc": 0.93},
       "k-NN": {"precision": 0.78, "recall": 0.80, "auc": 0.84},
   }

   fig = pareto_tradeoff_bubble_interactive(models)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
