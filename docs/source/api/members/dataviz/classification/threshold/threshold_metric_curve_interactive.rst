dataviz.classification.threshold.threshold_metric_curve_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold</p></div>

.. currentmodule:: dataviz.classification.threshold

.. autofunction:: threshold_metric_curve_interactive

Use case
--------

Use to pick an operating threshold; sweeps precision, recall, F1, accuracy, and specificity across thresholds.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold import threshold_metric_curve_interactive

   rng = np.random.default_rng(42)
   # churn model: pick an operating threshold balancing precision and recall
   n = 150
   y_true = (rng.random(n) < 0.3).astype(int)
   y_prob = np.clip(
       y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

   fig = threshold_metric_curve_interactive(
       y_true, y_prob,
       metrics=("precision", "recall", "f1", "specificity"),
       title="Churn model: metrics vs threshold")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold/threshold_metric_curve_interactive.png" alt="threshold_metric_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
