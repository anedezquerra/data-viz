dataviz.classification.model_comparison.metrics_radar_chart_interactive
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: metrics_radar_chart_interactive

Use case
--------

Compare several models across the same metric set at a glance with a radar/spider chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.classification.model_comparison import (
       metrics_radar_chart_interactive,
   )

   metrics = {
       "Logistic regression": {"accuracy": 0.82, "precision": 0.78,
                               "recall": 0.71, "f1": 0.74, "auc": 0.85},
       "Random forest": {"accuracy": 0.88, "precision": 0.85,
                         "recall": 0.80, "f1": 0.82, "auc": 0.91},
       "Gradient boosting": {"accuracy": 0.89, "precision": 0.87,
                             "recall": 0.79, "f1": 0.83, "auc": 0.92},
   }

   fig = metrics_radar_chart_interactive(
       metrics, title="Churn model bake-off: cross-validated metrics",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/metrics_radar_chart_interactive.png" alt="metrics_radar_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
