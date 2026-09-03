dataviz.regression.comparison.error_ecdf_overlay_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: error_ecdf_overlay_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.comparison import error_ecdf_overlay_static

   rng = np.random.default_rng(42)
   errors_per_model = [
       np.abs(rng.normal(0.0, 0.5, size=60)),
       np.abs(rng.normal(0.0, 0.8, size=60)),
   ]

   ax = error_ecdf_overlay_static(errors_per_model, ["OLS", "Ridge"])
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/comparison/error_ecdf_overlay_static.png" alt="error_ecdf_overlay_static example output"><figcaption>Example output</figcaption></figure></div>
