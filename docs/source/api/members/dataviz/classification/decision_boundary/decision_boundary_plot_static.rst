dataviz.classification.decision_boundary.decision_boundary_plot_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.decision_boundary</p></div>

.. currentmodule:: dataviz.classification.decision_boundary

.. autofunction:: decision_boundary_plot_static

Use case
--------

Use to visualize how a 2-D classifier partitions feature space, given any predict function over (n, 2) points.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.decision_boundary import decision_boundary_plot_static

   rng = np.random.default_rng(42)
   n = 120
   x = rng.uniform(-3, 3, n)
   y = rng.uniform(-3, 3, n)
   labels = (x ** 2 + y ** 2 + rng.normal(0, 0.4, n) > 2.5).astype(int)


   def knn_predict(points, k=5):
       train = np.column_stack([x, y])
       d = ((points[:, None, :] - train[None, :, :]) ** 2).sum(axis=2)
       nearest = np.argsort(d, axis=1)[:, :k]
       return (labels[nearest].mean(axis=1) >= 0.5).astype(int)


   ax = decision_boundary_plot_static(
       x, y, labels, knn_predict, resolution=100,
       title="5-NN ring classifier: decision boundary",
   )
   ax.set_xlabel("sensor reading A")
   ax.set_ylabel("sensor reading B")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/decision_boundary/decision_boundary_plot_static.png" alt="decision_boundary_plot_static example output"><figcaption>Example output</figcaption></figure></div>
