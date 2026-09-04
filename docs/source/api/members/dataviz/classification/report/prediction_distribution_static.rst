dataviz.classification.report.prediction_distribution_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.report</p></div>

.. currentmodule:: dataviz.classification.report

.. autofunction:: prediction_distribution_static

Use case
--------

Use to see, per true class, how predictions split across predicted classes; a row-normalized view of the confusion matrix.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.report import prediction_distribution_static

   rng = np.random.default_rng(42)
   # 3-class wine-quality model: where do predictions go per true class?
   labels = ["low", "medium", "high"]
   y_true = np.array([labels[i] for i in rng.choice(3, 150, p=[0.3, 0.5, 0.2])])
   y_pred = y_true.copy()
   adjacent = rng.random(150) < 0.22  # errors land on neighbouring grades
   idx = {l: k for k, l in enumerate(labels)}
   for i in np.where(adjacent)[0]:
       k = idx[y_pred[i]]
       y_pred[i] = labels[min(max(k + rng.choice([-1, 1]), 0), 2)]

   ax = prediction_distribution_static(y_true, y_pred, labels=labels,
                                       title="Wine-quality model: predicted share per grade")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/report/prediction_distribution_static.png" alt="prediction_distribution_static example output"><figcaption>Example output</figcaption></figure></div>
