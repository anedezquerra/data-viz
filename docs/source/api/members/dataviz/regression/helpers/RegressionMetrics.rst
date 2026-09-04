dataviz.regression.helpers.RegressionMetrics
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autoclass:: RegressionMetrics
   :members:
   :show-inheritance:

Use case
--------

Returned by compute_regression_metrics; carries the summary metrics (e.g., MAE, RMSE, R2) for a regression prediction.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.helpers import RegressionMetrics

   y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])
   y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])
   train_sizes = np.array([50, 100, 200])
   train_scores = np.array([0.82, 0.86, 0.89])
   validation_scores = np.array([0.76, 0.81, 0.84])

   result = RegressionMetrics(n=5, mae=0.5, mse=0.5, rmse=0.5, medae=0.5, mape=0.5, smape=0.5, r2=0.5, adj_r2=0.5, explained_variance=0.5, max_error=0.5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
