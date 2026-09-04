dataviz.regression.helpers.conformal_quantile
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autofunction:: conformal_quantile

Use case
--------

Use to get the split-conformal quantile of absolute residuals for distribution-free interval calibration.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.helpers import conformal_quantile

   rng = np.random.default_rng(42)
   calibration_residuals = pd.Series(rng.normal(0.0, 2.5, 30),
                                     name="calibration_residuals_ppm")
   q90 = conformal_quantile(calibration_residuals, alpha=0.1)
   print(f"90% conformal half-width: {q90:.3f} ppm")

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
