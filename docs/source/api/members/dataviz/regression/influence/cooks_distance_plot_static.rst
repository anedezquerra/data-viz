dataviz.regression.influence.cooks_distance_plot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.influence</p></div>

.. currentmodule:: dataviz.regression.influence

.. autofunction:: cooks_distance_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.influence import cooks_distance_plot_static

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(60, 3))
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)

   ax = cooks_distance_plot_static(X, y_true, y_pred)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/influence/cooks_distance_plot_static.png" alt="cooks_distance_plot_static example output"><figcaption>Example output</figcaption></figure></div>
