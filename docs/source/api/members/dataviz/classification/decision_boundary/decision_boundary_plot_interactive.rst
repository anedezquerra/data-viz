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
   from dataviz.classification.decision_boundary import decision_boundary_plot_interactive

   rng = np.random.default_rng(42)
   x = rng.normal(size=120)
   y = rng.normal(size=120)
   labels = (x + y > 0).astype(int)

   def predict_fn(points):
       return (points[:, 0] + points[:, 1] > 0).astype(int)

   fig = decision_boundary_plot_interactive(x, y, labels, predict_fn, resolution=60)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/decision_boundary/decision_boundary_plot_interactive.png" alt="decision_boundary_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
