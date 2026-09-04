dataviz.classification.pr_curve.precision_recall_curve_interactive
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.pr_curve</p></div>

.. currentmodule:: dataviz.classification.pr_curve

.. autofunction:: precision_recall_curve_interactive

Use case
--------

Use for imbalanced binary problems; plots precomputed precision vs recall with an optional AP value in the legend.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.pr_curve import precision_recall_curve_interactive

   rng = np.random.default_rng(42)
   n = 150
   # rare-event fraud detector: only 8% of transactions are fraud
   y_true = (rng.random(n) < 0.08).astype(int)
   y_prob = np.clip(
       y_true * rng.beta(6, 2, n) + (1 - y_true) * rng.beta(2, 8, n), 0, 1)
   order = np.argsort(-y_prob)
   precision, recall, tp, fp = [1.0], [0.0], 0, 0
   for i in order:
       if y_true[i] == 1:
           tp += 1
       else:
           fp += 1
       precision.append(tp / max(tp + fp, 1))
       recall.append(tp / max((y_true == 1).sum(), 1))
   ap = float(np.trapezoid(precision, recall))

   fig = precision_recall_curve_interactive(precision, recall, ap=abs(ap),
                                            title="Fraud detector precision-recall")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/pr_curve/precision_recall_curve_interactive.png" alt="precision_recall_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
