dataviz.univariate.charts.density_plot
======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.charts</p></div>

.. currentmodule:: dataviz.univariate.charts

.. autofunction:: density_plot

Use case
--------

Use to view a smooth kernel density estimate of a numeric variable when bin edges of a histogram would distract.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.charts import density_plot

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = density_plot(values)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/charts/density_plot.png" alt="density_plot example output"><figcaption>Example output</figcaption></figure></div>
