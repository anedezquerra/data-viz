dataviz.regression.helpers.InfluenceStatistics
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autoclass:: InfluenceStatistics
   :members:
   :show-inheritance:

Use case
--------

Returned by influence_statistics; carries per-observation leverage, Cook's distance, DFFITS, and DFBETAS.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.helpers import InfluenceStatistics

   rng = np.random.default_rng(42)
   n = 30
   square_feet = rng.uniform(900.0, 3500.0, n)
   bedrooms = rng.integers(1, 6, n).astype(float)
   age_years = rng.uniform(0.0, 40.0, n)
   X = pd.DataFrame({"square_feet": square_feet, "bedrooms": bedrooms,
                      "age_years": age_years})
   y = pd.Series(60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
                 + rng.normal(0.0, 15.0, n), name="price_kusd")

   result = InfluenceStatistics(
       leverage=np.full(n, 2.0 / n), residuals=rng.normal(0.0, 10.0, n),
       standardized_residuals=rng.normal(0.0, 1.0, n),
       studentized_residuals=rng.normal(0.0, 1.0, n),
       cooks_distance=np.abs(rng.normal(0.0, 0.05, n)),
       dffits=rng.normal(0.0, 0.3, n),
       dfbetas=rng.normal(0.0, 0.2, (n, 4)),
       sigma_hat=12.4, n_features=3)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
