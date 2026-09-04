dataviz.classification.multiclass.roc_curve_comparison_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: roc_curve_comparison_static

Use case
--------

Use to overlay ROC curves from several candidate models on one axes and pick the best discriminator by AUC.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass import roc_curve_comparison_static

   rng = np.random.default_rng(42)
   # churn screening: compare three candidate models on the same holdout
   n = 150
   y_true = (rng.random(n) < 0.3).astype(int)

   def roc(scores):
       order = np.argsort(-scores)
       fpr, tpr, tp, fp = [0.0], [0.0], 0, 0
       for i in order:
           if y_true[i] == 1:
               tp += 1
           else:
               fp += 1
           tpr.append(tp / max(y_true.sum(), 1))
           fpr.append(fp / max((1 - y_true).sum(), 1))
       return np.array(fpr), np.array(tpr)

   def scores(a_pos, b_pos, a_neg, b_neg):
       return np.clip(y_true * rng.beta(a_pos, b_pos, n)
                      + (1 - y_true) * rng.beta(a_neg, b_neg, n), 0, 1)

   models = {
       "Gradient boosting": roc(scores(8, 2, 2, 8)),
       "Logistic regression": roc(scores(6, 3, 3, 6)),
       "Naive Bayes": roc(scores(4, 3, 3, 4)),
   }

   ax = roc_curve_comparison_static(models,
                                    title="Churn models: ROC comparison")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass/roc_curve_comparison_static.png" alt="roc_curve_comparison_static example output"><figcaption>Example output</figcaption></figure></div>
