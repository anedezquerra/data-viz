dataviz.regression.comparison.residual_density_overlay_multi_static
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: residual_density_overlay_multi_static

Use case
--------

Use to compare residual distributions across models; tighter, zero-centered KDEs indicate better calibrated errors.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.comparison import residual_density_overlay_multi_static

   rng = np.random.default_rng(42)
   residuals_per_model = [
       rng.normal(0.0, 0.5, size=60),
       rng.normal(0.0, 0.8, size=60),
   ]

   ax = residual_density_overlay_multi_static(residuals_per_model, ["OLS", "Ridge"])
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/residual_density_overlay_multi_static.png" alt="residual_density_overlay_multi_static example output"><figcaption>Example output</figcaption></figure></div>
