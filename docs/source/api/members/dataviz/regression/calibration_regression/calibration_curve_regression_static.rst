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
   import matplotlib.pyplot as plt
   from dataviz.regression.calibration_regression import calibration_curve_regression_static

   y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])
   y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])
   train_sizes = np.array([50, 100, 200])
   train_scores = np.array([0.82, 0.86, 0.89])
   validation_scores = np.array([0.76, 0.81, 0.84])

   ax = calibration_curve_regression_static(y_true, y_pred)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/calibration_regression/calibration_curve_regression_static.png" alt="calibration_curve_regression_static example output"><figcaption>Example output</figcaption></figure></div>
