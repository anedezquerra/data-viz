dataviz.regression.gof.residual_dependence_test_panel_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.gof</p></div>

.. currentmodule:: dataviz.regression.gof

.. autofunction:: residual_dependence_test_panel_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.gof import residual_dependence_test_panel_static

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(60, 3))
   residuals = rng.normal(0.0, 1.0, size=60)

   result = residual_dependence_test_panel_static(X, residuals)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/gof/residual_dependence_test_panel_static.png" alt="residual_dependence_test_panel_static example output"><figcaption>Example output</figcaption></figure></div>
