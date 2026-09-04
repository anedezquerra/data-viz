dataviz.classification.charts.roc_curve
=======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.charts</p></div>

.. currentmodule:: dataviz.classification.charts

.. autofunction:: roc_curve

Use case
--------

Use to summarize ranking quality across all thresholds from known fpr/tpr arrays, with optional AUC in the legend.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.charts import roc_curve

   rng = np.random.default_rng(42)
   n_pos, n_neg = 50, 110
   y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
   y_score = np.concatenate([
       rng.normal(0.68, 0.16, n_pos),
       rng.normal(0.32, 0.16, n_neg),
   ]).clip(0.0, 1.0)

   thresholds = np.linspace(1.0, 0.0, 101)
   tpr = [(y_score[y_true == 1] >= t).mean() for t in thresholds]
   fpr = [(y_score[y_true == 0] >= t).mean() for t in thresholds]
   auc = float(np.trapezoid(tpr, fpr))

   ax = roc_curve(
       fpr, tpr, auc=abs(auc),
       title="Fraud screening model: ROC curve", color="tab:blue",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/charts/roc_curve.png" alt="roc_curve example output"><figcaption>Example output</figcaption></figure></div>
