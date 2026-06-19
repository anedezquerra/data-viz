dataviz.spc.multivariate.HotellingT2Result
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.spc.multivariate</p></div>

.. currentmodule:: dataviz.spc.multivariate

.. autoclass:: HotellingT2Result
   :members:
   :show-inheritance:

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.multivariate import HotellingT2Result
   import pandas as pd

   rng = np.random.default_rng(42)
   data = rng.multivariate_normal([10.0, 25.0, 4.0], [[1.0, 0.5, 0.2], [0.5, 2.0, 0.3], [0.2, 0.3, 0.5]], size=40)

   result = HotellingT2Result(scores=pd.Series([0.5, 1.2], name="T2"), center=pd.Series([10.0, 25.0]), covariance=pd.DataFrame([[1.0, 0.2], [0.2, 2.0]]), limit=1.1)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
