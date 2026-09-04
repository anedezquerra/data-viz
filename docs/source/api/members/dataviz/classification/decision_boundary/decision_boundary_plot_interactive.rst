dataviz.classification.decision_boundary.decision_boundary_plot_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.decision_boundary</p></div>

.. currentmodule:: dataviz.classification.decision_boundary

.. autofunction:: decision_boundary_plot_interactive

Use case
--------

Use to visualize how a 2-D classifier partitions feature space, given any predict function over (n, 2) points.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.decision_boundary import (
       decision_boundary_plot_interactive,
   )

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


   fig = decision_boundary_plot_interactive(
       x, y, labels, knn_predict, resolution=80,
       title="5-NN ring classifier: decision boundary",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/decision_boundary/decision_boundary_plot_interactive.png" alt="decision_boundary_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
