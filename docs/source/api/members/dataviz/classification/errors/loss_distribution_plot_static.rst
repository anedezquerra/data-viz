dataviz.classification.errors.loss_distribution_plot_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.errors</p></div>

.. currentmodule:: dataviz.classification.errors

.. autofunction:: loss_distribution_plot_static

Use case
--------

Use to surface high-loss outlier samples driving log loss, split by true class with the mean marked.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.errors import loss_distribution_plot_static

   rng = np.random.default_rng(43)
   n = 160
   signal = rng.normal(0, 1.3, n)
   y_prob = np.clip(1.0 / (1.0 + np.exp(-signal)), 1e-4, 1 - 1e-4)
   y_true = (signal + rng.normal(0, 0.9, n) > 0).astype(int)
   # a few hard mislabeled samples create high-loss outliers
   y_true[:4] = 1 - y_true[:4]
   y_prob[:4] = np.clip(y_prob[:4], 0.85, 0.98)

   ax = loss_distribution_plot_static(
       y_true, y_prob, bins=30,
       title="Document classifier: per-sample log loss outlier hunt",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/errors/loss_distribution_plot_static.png" alt="loss_distribution_plot_static example output"><figcaption>Example output</figcaption></figure></div>
