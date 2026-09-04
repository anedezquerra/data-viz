dataviz.regression.autocorrelation.residual_acf_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.autocorrelation</p></div>

.. currentmodule:: dataviz.regression.autocorrelation

.. autofunction:: residual_acf_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.autocorrelation import residual_acf_interactive

   rng = np.random.default_rng(42)
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)

   fig = residual_acf_interactive(y_true, y_pred, max_lag=10)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/autocorrelation/residual_acf_interactive.png" alt="residual_acf_interactive example output"><figcaption>Example output</figcaption></figure></div>
