dataviz.classification.model_comparison.pareto_tradeoff_bubble_interactive
==========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: pareto_tradeoff_bubble_interactive

Use case
--------

Compare models on two competing metrics and highlight the Pareto frontier of non-dominated candidates.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.classification.model_comparison import (
       pareto_tradeoff_bubble_interactive,
   )

   models = {
       "logreg": {"precision": 0.78, "recall": 0.72, "auc": 0.85},
       "rf-shallow": {"precision": 0.83, "recall": 0.75, "auc": 0.89},
       "rf-deep": {"precision": 0.86, "recall": 0.70, "auc": 0.91},
       "gbm": {"precision": 0.84, "recall": 0.81, "auc": 0.92},
       "knn": {"precision": 0.70, "recall": 0.65, "auc": 0.76},
       "mlp": {"precision": 0.80, "recall": 0.78, "auc": 0.88},
   }

   fig = pareto_tradeoff_bubble_interactive(
       models, x_metric="precision", y_metric="recall", size_metric="auc",
       title="Fraud models: precision-recall trade-off (bubble = AUC)",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/pareto_tradeoff_bubble_interactive.png" alt="pareto_tradeoff_bubble_interactive example output"><figcaption>Example output</figcaption></figure></div>
