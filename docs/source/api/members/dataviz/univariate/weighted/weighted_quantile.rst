dataviz.univariate.weighted.weighted_quantile
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.weighted</p></div>

.. currentmodule:: dataviz.univariate.weighted

.. autofunction:: weighted_quantile

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.weighted import weighted_quantile

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")
   weights = pd.Series([1.0, 1.5, 0.8, 1.2, 1.0, 1.1], name="Weight")

   result = weighted_quantile(values, weights, quantile=0.5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
