dataviz.regression.residual_extended.residual_boxplot_by_group_static
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: residual_boxplot_by_group_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.residual_extended import residual_boxplot_by_group_static

   rng = np.random.default_rng(42)
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)
   groups = rng.choice(["A", "B", "C"], size=60)

   ax = residual_boxplot_by_group_static(y_true, y_pred, groups)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/residual_boxplot_by_group_static.png" alt="residual_boxplot_by_group_static example output"><figcaption>Example output</figcaption></figure></div>
