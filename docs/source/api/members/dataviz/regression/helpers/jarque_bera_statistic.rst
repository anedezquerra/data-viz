dataviz.regression.helpers.jarque_bera_statistic
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autofunction:: jarque_bera_statistic

Use case
--------

Use to compute the Jarque-Bera statistic and p-value when testing residuals for normality.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.helpers import jarque_bera_statistic

   rng = np.random.default_rng(42)
   noise = rng.normal(0.0, 1.0, 30)
   residuals = pd.Series(
       np.array([noise[0]] + [0.55 * noise[i - 1] + noise[i] for i in range(1, 30)]),
       index=pd.date_range("2025-01-01", periods=30, freq="D"),
       name="streamflow_residuals")

   result = jarque_bera_statistic(residuals)
   print(f"JB={result[0]:.3f}, p-value={result[1]:.4f}")

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
