dataviz.classification.multiclass.multiclass_pr_curve_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: multiclass_pr_curve_static

Use case
--------

Use when comparing one-vs-rest precision-recall trade-offs across classes, especially on imbalanced multiclass problems where ROC looks overly optimistic.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass import multiclass_pr_curve_static

   rng = np.random.default_rng(42)
   # 3-class support-ticket triage model, one-vs-rest PR per class
   def ovr_pr(scores, truth):
       order = np.argsort(-scores)
       precision, recall, tp, fp = [1.0], [0.0], 0, 0
       for i in order:
           if truth[i] == 1:
               tp += 1
           else:
               fp += 1
           precision.append(tp / max(tp + fp, 1))
           recall.append(tp / max(truth.sum(), 1))
       return np.array(recall), np.array(precision)

   n = 120
   y = rng.integers(0, 3, n)
   curves = {}
   for k, name in enumerate(["Billing", "Technical", "Account"]):
       truth = (y == k).astype(int)
       score = np.clip(truth * rng.beta(6, 3, n) + (1 - truth) * rng.beta(3, 6, n), 0, 1)
       curves[name] = ovr_pr(score, truth)

   ax = multiclass_pr_curve_static(curves,
                                   title="Ticket triage: one-vs-rest PR")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass/multiclass_pr_curve_static.png" alt="multiclass_pr_curve_static example output"><figcaption>Example output</figcaption></figure></div>
