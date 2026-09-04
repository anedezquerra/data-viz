dataviz.classification.report.class_balance_bar_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.report</p></div>

.. currentmodule:: dataviz.classification.report

.. autofunction:: class_balance_bar_static

Use case
--------

Use before training to check target imbalance, or after to compare predicted class counts against ground truth.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.report import class_balance_bar_static

   rng = np.random.default_rng(42)
   # imbalanced support-ticket queue: does the model under-predict "urgent"?
   labels = ["low", "normal", "high", "urgent"]
   y_true = np.array([labels[i] for i in rng.choice(4, 140, p=[0.4, 0.35, 0.18, 0.07])])
   y_pred = y_true.copy()
   shift = rng.random(140) < 0.2
   y_pred[shift] = "normal"  # model collapses rare classes toward "normal"

   ax = class_balance_bar_static(y_true, y_pred, labels=labels,
                                 title="Ticket priority: true vs predicted balance")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/report/class_balance_bar_static.png" alt="class_balance_bar_static example output"><figcaption>Example output</figcaption></figure></div>
