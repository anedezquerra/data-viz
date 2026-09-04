dataviz.classification.model_comparison.metrics_radar_chart_interactive
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: metrics_radar_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.model_comparison import metrics_radar_chart_interactive

   metrics = {
       "Logistic regression": {"accuracy": 0.84, "precision": 0.81, "recall": 0.86, "f1": 0.83},
       "Random forest": {"accuracy": 0.89, "precision": 0.88, "recall": 0.90, "f1": 0.89},
       "Gradient boosting": {"accuracy": 0.87, "precision": 0.85, "recall": 0.89, "f1": 0.87},
   }

   fig = metrics_radar_chart_interactive(metrics)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/metrics_radar_chart_interactive.png" alt="metrics_radar_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
