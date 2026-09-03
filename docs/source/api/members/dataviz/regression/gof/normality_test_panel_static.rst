dataviz.regression.gof.normality_test_panel_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.gof</p></div>

.. currentmodule:: dataviz.regression.gof

.. autofunction:: normality_test_panel_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.gof import normality_test_panel_static

   rng = np.random.default_rng(42)
   residuals = rng.normal(0.0, 1.0, size=80)

   result = normality_test_panel_static(residuals)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/gof/normality_test_panel_static.png" alt="normality_test_panel_static example output"><figcaption>Example output</figcaption></figure></div>
