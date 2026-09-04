dataviz.spc.multivariate.hotelling_t2_summary
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.multivariate</p></div>

.. currentmodule:: dataviz.spc.multivariate

.. autofunction:: hotelling_t2_summary

Use case
--------

Use to compute Hotelling T-squared scores when several correlated process variables must be monitored jointly rather than on separate charts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.spc.multivariate import hotelling_t2_summary

   rng = np.random.default_rng(42)
   # 30 hourly readings of correlated reactor variables
   temp = rng.normal(180.0, 1.5, size=30)
   pressure = 4.0 + 0.02 * (temp - 180.0) + rng.normal(0.0, 0.05, size=30)
   flow = rng.normal(12.0, 0.4, size=30)
   temp[24] = 185.8  # heater excursion
   df = pd.DataFrame({"temp": temp, "pressure": pressure, "flow": flow})

   result = hotelling_t2_summary(df, limit_quantile=0.99)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
