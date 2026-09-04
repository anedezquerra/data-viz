dataviz.classification.confusion_matrix.confusion_matrix_plot_static
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.confusion_matrix</p></div>

.. currentmodule:: dataviz.classification.confusion_matrix

.. autofunction:: confusion_matrix_plot_static

Use case
--------

Use for a publication-style confusion matrix heatmap with counts, labels and colorbar.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.confusion_matrix import confusion_matrix_plot_static

   rng = np.random.default_rng(42)
   n = 160
   y_prob = np.clip(rng.beta(2, 4, n), 0.01, 0.99)
   y_true = (rng.uniform(size=n) < y_prob).astype(int)
   y_pred = (y_prob >= 0.35).astype(int)  # low threshold: fraud recall first
   cm = np.zeros((2, 2), dtype=int)
   for t, p in zip(y_true, y_pred):
       cm[t, p] += 1

   ax = confusion_matrix_plot_static(
       cm, labels=["legitimate", "fraud"],
       title="Fraud detector at 0.35 alert threshold",
       cmap="Oranges",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/confusion_matrix/confusion_matrix_plot_static.png" alt="confusion_matrix_plot_static example output"><figcaption>Example output</figcaption></figure></div>
