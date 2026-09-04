dataviz.regression.helpers.white_test_statistic
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autofunction:: white_test_statistic

Use case
--------

Use to compute the White test statistic when checking heteroscedasticity without assuming its form.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.helpers import white_test_statistic

   rng = np.random.default_rng(42)
   n = 30
   square_feet = rng.uniform(900.0, 3500.0, n)
   bedrooms = rng.integers(1, 6, n).astype(float)
   age_years = rng.uniform(0.0, 40.0, n)
   X = pd.DataFrame({"square_feet": square_feet, "bedrooms": bedrooms,
                      "age_years": age_years})
   y = pd.Series(60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
                 + rng.normal(0.0, 15.0, n), name="price_kusd")

   y_pred = 60.0 + 0.16 * square_feet + 10.0 * bedrooms - 0.8 * age_years
   residuals = y - y_pred + square_feet / 500.0
   result = white_test_statistic(X, residuals)
   print(f"LM={result[0]:.3f}, p-value={result[1]:.4f}")

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
