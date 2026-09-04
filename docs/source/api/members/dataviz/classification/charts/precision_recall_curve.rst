dataviz.classification.charts.precision_recall_curve
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.charts</p></div>

.. currentmodule:: dataviz.classification.charts

.. autofunction:: precision_recall_curve

Use case
--------

Use when tuning a classifier's decision threshold to trade off precision against recall, especially on imbalanced data.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.charts import precision_recall_curve

   rng = np.random.default_rng(42)
   n_pos, n_neg = 40, 120
   y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
   y_score = np.concatenate([
       rng.normal(0.70, 0.17, n_pos),
       rng.normal(0.30, 0.15, n_neg),
   ]).clip(0.0, 1.0)

   thresholds = np.linspace(1.0, 0.0, 101)
   precision, recall = [], []
   for t in thresholds:
       flagged = y_score >= t
       tp = int((flagged & (y_true == 1)).sum())
       fp = int((flagged & (y_true == 0)).sum())
       fn = int((~flagged & (y_true == 1)).sum())
       precision.append(tp / (tp + fp) if tp + fp else 1.0)
       recall.append(tp / (tp + fn) if tp + fn else 0.0)
   ap = float(np.trapezoid(precision[::-1], recall[::-1]))

   ax = precision_recall_curve(
       precision, recall, ap=abs(ap),
       title="Rare-disease screening: precision-recall curve", color="tab:green",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/charts/precision_recall_curve.png" alt="precision_recall_curve example output"><figcaption>Example output</figcaption></figure></div>
