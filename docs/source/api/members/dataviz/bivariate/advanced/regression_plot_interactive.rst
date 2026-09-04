dataviz.bivariate.advanced.regression_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: regression_plot_interactive

Use case
--------

Use to overlay a polynomial trend line on a scatter plot when assessing whether a simple curve fits the relationship.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.bivariate.advanced import regression_plot_interactive

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")

   fig = regression_plot_interactive(x, y)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/regression_plot_interactive.png" alt="regression_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
