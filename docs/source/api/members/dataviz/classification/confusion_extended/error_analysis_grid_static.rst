dataviz.classification.confusion_extended.error_analysis_grid_static
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.confusion_extended</p></div>

.. currentmodule:: dataviz.classification.confusion_extended

.. autofunction:: error_analysis_grid_static

Use case
--------

Use to isolate which class pairs get confused; shows only off-diagonal mistake rates per true class.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.confusion_extended import error_analysis_grid_static

   rng = np.random.default_rng(23)
   n = 200
   true_labels = rng.choice(4, size=n, p=[0.4, 0.3, 0.2, 0.1])
   pred_labels = true_labels.copy()
   flip = rng.uniform(size=n) < 0.2
   pred_labels[flip] = np.clip(true_labels[flip] + rng.choice([-1, 1],
                               size=int(flip.sum())), 0, 3)
   cm = np.zeros((4, 4), dtype=int)
   for t, p in zip(true_labels, pred_labels):
       cm[t, p] += 1
   classes = ["sedan", "SUV", "truck", "van"]

   ax = error_analysis_grid_static(
       cm, labels=classes,
       title="Vehicle image classifier: which classes get confused?",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/confusion_extended/error_analysis_grid_static.png" alt="error_analysis_grid_static example output"><figcaption>Example output</figcaption></figure></div>
