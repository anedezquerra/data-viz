dataviz.classification.decision_boundary.decision_boundary_plot_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.decision_boundary</p></div>

.. currentmodule:: dataviz.classification.decision_boundary

.. autofunction:: decision_boundary_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.decision_boundary import decision_boundary_plot_static

   rng = np.random.default_rng(42)
   x = rng.normal(size=120)
   y = rng.normal(size=120)
   labels = (x + y > 0).astype(int)

   def predict_fn(points):
       return (points[:, 0] + points[:, 1] > 0).astype(int)

   ax = decision_boundary_plot_static(x, y, labels, predict_fn, resolution=80)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
