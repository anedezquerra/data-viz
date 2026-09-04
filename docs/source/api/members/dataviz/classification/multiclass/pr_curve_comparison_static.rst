dataviz.classification.multiclass.pr_curve_comparison_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: pr_curve_comparison_static

Use case
--------

Use to compare candidate models on average precision when positives are rare; overlays one PR curve per model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass import pr_curve_comparison_static

   rng = np.random.default_rng(42)
   # fraud screening: PR comparison matters under heavy class imbalance
   n = 150
   y_true = (rng.random(n) < 0.08).astype(int)

   def pr(scores):
       order = np.argsort(-scores)
       precision, recall, tp, fp = [1.0], [0.0], 0, 0
       for i in order:
           if y_true[i] == 1:
               tp += 1
           else:
               fp += 1
           precision.append(tp / max(tp + fp, 1))
           recall.append(tp / max(y_true.sum(), 1))
       return np.array(recall), np.array(precision)

   def scores(a_pos, b_pos, a_neg, b_neg):
       return np.clip(y_true * rng.beta(a_pos, b_pos, n)
                      + (1 - y_true) * rng.beta(a_neg, b_neg, n), 0, 1)

   models = {
       "Gradient boosting": pr(scores(8, 2, 2, 8)),
       "Logistic regression": pr(scores(6, 3, 3, 6)),
       "Naive Bayes": pr(scores(4, 3, 3, 4)),
   }

   ax = pr_curve_comparison_static(models,
                                   title="Fraud models: PR comparison")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass/pr_curve_comparison_static.png" alt="pr_curve_comparison_static example output"><figcaption>Example output</figcaption></figure></div>
