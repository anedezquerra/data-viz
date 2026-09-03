dataviz.classification.model_comparison.metrics_radar_chart_static
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: metrics_radar_chart_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.model_comparison import metrics_radar_chart_static

   metrics = {
       "Logistic regression": {"accuracy": 0.84, "precision": 0.81, "recall": 0.86, "f1": 0.83},
       "Random forest": {"accuracy": 0.89, "precision": 0.88, "recall": 0.90, "f1": 0.89},
       "Gradient boosting": {"accuracy": 0.87, "precision": 0.85, "recall": 0.89, "f1": 0.87},
   }

   ax = metrics_radar_chart_static(metrics)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
