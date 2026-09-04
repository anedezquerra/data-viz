dataviz.univariate.charts.histogram
===================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.charts</p></div>

.. currentmodule:: dataviz.univariate.charts

.. autofunction:: histogram

Use case
--------

Use when profiling a numeric column for the first time to see shape, spread, and outliers at a glance.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.charts import histogram

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = histogram(values)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/charts/histogram.png" alt="histogram example output"><figcaption>Example output</figcaption></figure></div>
