dataviz.regression.autocorrelation.residual_pacf_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.autocorrelation</p></div>

.. currentmodule:: dataviz.regression.autocorrelation

.. autofunction:: residual_pacf_static

Use case
--------

Use to identify the direct lag order of residual dependence when choosing an AR term or diagnosing model misspecification.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.autocorrelation import residual_pacf_static

   rng = np.random.default_rng(42)
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)

   ax = residual_pacf_static(y_true, y_pred, max_lag=10)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/autocorrelation/residual_pacf_static.png" alt="residual_pacf_static example output"><figcaption>Example output</figcaption></figure></div>
