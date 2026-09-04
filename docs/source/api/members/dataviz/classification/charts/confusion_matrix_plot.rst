dataviz.classification.charts.confusion_matrix_plot
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.charts</p></div>

.. currentmodule:: dataviz.classification.charts

.. autofunction:: confusion_matrix_plot

Use case
--------

Use for a quick annotated confusion matrix heatmap of actual vs. predicted class counts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.charts import confusion_matrix_plot

   rng = np.random.default_rng(42)
   n = 150
   true_labels = rng.choice(3, size=n, p=[0.5, 0.3, 0.2])
   pred_labels = true_labels.copy()
   flip = rng.uniform(size=n) < 0.18
   pred_labels[flip] = rng.choice(3, size=int(flip.sum()))
   classes = ["retained", "at-risk", "churned"]
   cm = np.zeros((3, 3), dtype=int)
   for t, p in zip(true_labels, pred_labels):
       cm[t, p] += 1

   ax = confusion_matrix_plot(
       cm, labels=classes, title="Customer retention model: confusion matrix",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/charts/confusion_matrix_plot.png" alt="confusion_matrix_plot example output"><figcaption>Example output</figcaption></figure></div>
