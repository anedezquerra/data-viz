dataviz.bivariate.scatter.scatter_plot_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.scatter</p></div>

.. currentmodule:: dataviz.bivariate.scatter

.. autofunction:: scatter_plot_static

Use case
--------

Use as a first look at the relationship between two numeric variables before choosing a more specialized view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.scatter import scatter_plot_static

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")

   ax = scatter_plot_static(x, y)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/scatter/scatter_plot_static.png" alt="scatter_plot_static example output"><figcaption>Example output</figcaption></figure></div>
