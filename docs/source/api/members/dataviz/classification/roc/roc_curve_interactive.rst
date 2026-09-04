dataviz.classification.roc.roc_curve_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.roc</p></div>

.. currentmodule:: dataviz.classification.roc

.. autofunction:: roc_curve_interactive

Use case
--------

Use to assess a binary classifier from precomputed fpr/tpr arrays, with optional AUC label and random-chance reference line.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.roc import roc_curve_interactive

   rng = np.random.default_rng(42)
   n = 150
   y_true = (rng.random(n) < 0.35).astype(int)  # churn flag, 35% prevalence
   y_prob = np.clip(
       y_true * rng.beta(7, 2.5, n) + (1 - y_true) * rng.beta(2.5, 7, n), 0, 1)
   order = np.argsort(-y_prob)
   fpr, tpr, tp, fp = [0.0], [0.0], 0, 0
   for i in order:
       if y_true[i] == 1:
           tp += 1
       else:
           fp += 1
       tpr.append(tp / max((y_true == 1).sum(), 1))
       fpr.append(fp / max((y_true == 0).sum(), 1))
   fpr, tpr = np.array(fpr), np.array(tpr)
   auc = float(np.trapezoid(tpr, fpr))

   fig = roc_curve_interactive(fpr, tpr, auc=auc,
                               title="Churn model ROC (holdout quarter)")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/roc/roc_curve_interactive.png" alt="roc_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
