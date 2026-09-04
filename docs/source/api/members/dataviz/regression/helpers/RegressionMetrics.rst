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
   import pandas as pd
   from dataviz.regression.helpers import RegressionMetrics

   rng = np.random.default_rng(42)
   n = 30
   square_feet = rng.uniform(900.0, 3500.0, n)
   bedrooms = rng.integers(1, 6, n).astype(float)
   age_years = rng.uniform(0.0, 40.0, n)
   X = pd.DataFrame({"square_feet": square_feet, "bedrooms": bedrooms,
                      "age_years": age_years})
   y = pd.Series(60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
                 + rng.normal(0.0, 15.0, n), name="price_kusd")

   result = RegressionMetrics(
       n=n, mae=11.2, mse=198.4, rmse=14.1, medae=9.3, mape=4.1, smape=4.0,
       r2=0.93, adj_r2=0.92, explained_variance=0.93, max_error=41.7)
   print(result)
   print(result.as_dict()["rmse"])

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
