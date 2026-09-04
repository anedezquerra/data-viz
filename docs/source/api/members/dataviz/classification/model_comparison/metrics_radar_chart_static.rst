dataviz.classification.model_comparison.metrics_radar_chart_static
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: metrics_radar_chart_static

Use case
--------

Compare several models across the same metric set at a glance with a radar/spider chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.classification.model_comparison import metrics_radar_chart_static

   metrics = {
       "Logistic regression": {"accuracy": 0.82, "precision": 0.78,
                               "recall": 0.71, "f1": 0.74, "auc": 0.85},
       "Random forest": {"accuracy": 0.88, "precision": 0.85,
                         "recall": 0.80, "f1": 0.82, "auc": 0.91},
       "Gradient boosting": {"accuracy": 0.89, "precision": 0.87,
                             "recall": 0.79, "f1": 0.83, "auc": 0.92},
   }

   ax = metrics_radar_chart_static(
       metrics, title="Churn model bake-off: cross-validated metrics",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/metrics_radar_chart_static.png" alt="metrics_radar_chart_static example output"><figcaption>Example output</figcaption></figure></div>
