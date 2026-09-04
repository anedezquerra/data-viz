dataviz.univariate.quality.data_quality_summary
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.quality</p></div>

.. currentmodule:: dataviz.univariate.quality

.. autofunction:: data_quality_summary

Use case
--------

Use as a first-pass screen of one variable for missingness, duplicates, zeros, and negatives before choosing downstream visualizations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.quality import data_quality_summary

   rng = np.random.default_rng(42)
   readings = rng.normal(loc=55.0, scale=4.0, size=140).round(2)
   readings[[3, 27, 58, 91, 120]] = np.nan
   readings[[10, 66, 101]] = -999.0
   sensor = pd.Series(readings, name="temperature_c")
   result = data_quality_summary(sensor)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
