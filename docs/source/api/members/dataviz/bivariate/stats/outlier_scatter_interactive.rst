dataviz.bivariate.stats.outlier_scatter_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: outlier_scatter_interactive

Use case
--------

Use to flag unusual points in a two-variable relationship using z-score or IQR rules before fitting models.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.bivariate.stats import outlier_scatter_interactive

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")

   fig = outlier_scatter_interactive(x, y)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/outlier_scatter_interactive.png" alt="outlier_scatter_interactive example output"><figcaption>Example output</figcaption></figure></div>
