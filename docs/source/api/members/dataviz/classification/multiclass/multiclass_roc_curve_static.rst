dataviz.classification.multiclass.multiclass_roc_curve_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: multiclass_roc_curve_static

Use case
--------

Use when evaluating a multiclass classifier one class at a time; plots one-vs-rest ROC per class with optional macro average and random baseline.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass import multiclass_roc_curve_static

   rng = np.random.default_rng(42)
   # 3-class support-ticket triage model, one-vs-rest ROC per class
   def ovr_roc(scores, truth):
       order = np.argsort(-scores)
       fpr, tpr, tp, fp = [0.0], [0.0], 0, 0
       for i in order:
           if truth[i] == 1:
               tp += 1
           else:
               fp += 1
           tpr.append(tp / max(truth.sum(), 1))
           fpr.append(fp / max((1 - truth).sum(), 1))
       return np.array(fpr), np.array(tpr)

   n = 120
   y = rng.integers(0, 3, n)
   curves = {}
   for k, name in enumerate(["Billing", "Technical", "Account"]):
       truth = (y == k).astype(int)
       score = np.clip(truth * rng.beta(6, 3, n) + (1 - truth) * rng.beta(3, 6, n), 0, 1)
       curves[name] = ovr_roc(score, truth)

   ax = multiclass_roc_curve_static(curves,
                                    title="Ticket triage: one-vs-rest ROC")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass/multiclass_roc_curve_static.png" alt="multiclass_roc_curve_static example output"><figcaption>Example output</figcaption></figure></div>
