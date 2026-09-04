dataviz.regression.transforms.power_transform_residual_panel_static
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.transforms</p></div>

.. currentmodule:: dataviz.regression.transforms

.. autofunction:: power_transform_residual_panel_static

Use case
--------

Compare residuals-vs-fitted for raw, log, and sqrt transforms side by side to choose the response transform that best stabilizes variance.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.transforms import power_transform_residual_panel_static

   rng = np.random.default_rng(42)
   y_pred = rng.normal(10.0, 2.0, size=60)
   residuals_orig = rng.normal(0.0, 1.2, size=60)
   residuals_log = residuals_orig * 0.6
   residuals_sqrt = residuals_orig * 0.8

   result = power_transform_residual_panel_static(
       y_pred, residuals_orig, residuals_log, residuals_sqrt
   )
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/transforms/power_transform_residual_panel_static.png" alt="power_transform_residual_panel_static example output"><figcaption>Example output</figcaption></figure></div>
