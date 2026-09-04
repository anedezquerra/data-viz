dataviz.spc.multivariate.HotellingT2Result
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.spc.multivariate</p></div>

.. currentmodule:: dataviz.spc.multivariate

.. autoclass:: HotellingT2Result
   :members:
   :show-inheritance:

Use case
--------

Carries T-squared scores, center vector, covariance matrix, and the control limit; consumed when charting or summarizing multivariate process stability.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.spc.multivariate import HotellingT2Result

   # T-squared monitoring result for a reactor temp/pressure loop
   scores = pd.Series([1.2, 2.0, 0.8, 5.4], name="T2")
   center = pd.Series({"temp": 180.0, "pressure": 4.2})
   covariance = pd.DataFrame(np.eye(2), index=["temp", "pressure"], columns=["temp", "pressure"])
   result = HotellingT2Result(scores=scores, center=center, covariance=covariance, limit=4.0)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
