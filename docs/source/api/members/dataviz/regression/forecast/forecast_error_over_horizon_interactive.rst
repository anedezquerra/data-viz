dataviz.regression.forecast.forecast_error_over_horizon_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: forecast_error_over_horizon_interactive

Use case
--------

Use to see how an error metric such as MAE or RMSE grows as the forecast horizon lengthens.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.forecast import forecast_error_over_horizon_interactive

   y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])
   y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])
   train_sizes = np.array([50, 100, 200])
   train_scores = np.array([0.82, 0.86, 0.89])
   validation_scores = np.array([0.76, 0.81, 0.84])

   fig = forecast_error_over_horizon_interactive(y_true, y_pred)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/forecast_error_over_horizon_interactive.png" alt="forecast_error_over_horizon_interactive example output"><figcaption>Example output</figcaption></figure></div>
