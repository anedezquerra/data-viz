dataviz.univariate.stats.univariate_summary
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.stats</p></div>

.. currentmodule:: dataviz.univariate.stats

.. autofunction:: univariate_summary

Use case
--------

Use for a complete descriptive summary of one numeric variable, including quartiles, skewness, kurtosis, SEM, and MAD.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.stats import univariate_summary

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = univariate_summary(values)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
