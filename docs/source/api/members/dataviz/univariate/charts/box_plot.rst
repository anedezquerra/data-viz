dataviz.univariate.charts.box_plot
==================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.charts</p></div>

.. currentmodule:: dataviz.univariate.charts

.. autofunction:: box_plot

Use case
--------

Use to summarize quartiles, spread, and outliers of a numeric variable in a compact box plot.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.charts import box_plot

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = box_plot(values)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/charts/box_plot.png" alt="box_plot example output"><figcaption>Example output</figcaption></figure></div>
