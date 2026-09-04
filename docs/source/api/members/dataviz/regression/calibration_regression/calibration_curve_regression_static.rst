dataviz.regression.calibration_regression.calibration_curve_regression_static
=============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.calibration_regression</p></div>

.. currentmodule:: dataviz.regression.calibration_regression

.. autofunction:: calibration_curve_regression_static

Use case
--------

Use when predicted values should match observed means in each bin; systematic deviation from the diagonal signals a miscalibrated regressor.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.calibration_regression import calibration_curve_regression_static

   rng = np.random.default_rng(42)
   n = 32
   pred_price = pd.Series(rng.uniform(180, 520, n), name="predicted_price_k")
   actual_price = pd.Series(pred_price * rng.normal(1.0, 0.08, n),
                            name="actual_price_k")

   ax = calibration_curve_regression_static(
       actual_price, pred_price, n_bins=6,
       title="Home Appraisal Model: Calibration Curve",
       color="#1f6fb2")
   ax.set_xlabel("Predicted price (bin mean, k USD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/calibration_regression/calibration_curve_regression_static.png" alt="calibration_curve_regression_static example output"><figcaption>Example output</figcaption></figure></div>
