dataviz.classification.report.per_class_metrics_bar_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.report</p></div>

.. currentmodule:: dataviz.classification.report

.. autofunction:: per_class_metrics_bar_static

Use case
--------

Use to compare precision, recall, and F1 side by side per class with grouped bars.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.report import per_class_metrics_bar_static

   rng = np.random.default_rng(42)
   # 4-class land-cover classifier on satellite tiles
   n = 160
   labels = ["forest", "water", "urban", "crops"]
   y_true = np.array([labels[i] for i in rng.integers(0, 4, n)])
   err = rng.random(n) < 0.15
   y_pred = y_true.copy()
   y_pred[err] = np.array([labels[i] for i in rng.integers(0, 4, err.sum())])

   ax = per_class_metrics_bar_static(y_true, y_pred, labels=labels,
                                     title="Land-cover classifier: precision / recall / F1")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/report/per_class_metrics_bar_static.png" alt="per_class_metrics_bar_static example output"><figcaption>Example output</figcaption></figure></div>
