dataviz.classification.threshold.cost_curve_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold</p></div>

.. currentmodule:: dataviz.classification.threshold

.. autofunction:: cost_curve_interactive

Use case
--------

Use when false positives and false negatives carry different costs; finds the threshold minimizing total misclassification cost.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold import cost_curve_interactive

   rng = np.random.default_rng(42)
   # fraud screening: a missed fraud costs 8x a false alarm review
   n = 150
   y_true = (rng.random(n) < 0.08).astype(int)
   y_prob = np.clip(
       y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 8, n), 0, 1)

   fig = cost_curve_interactive(y_true, y_prob, cost_fp=1.0, cost_fn=8.0,
                                title="Fraud screening: total cost vs threshold")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold/cost_curve_interactive.png" alt="cost_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
