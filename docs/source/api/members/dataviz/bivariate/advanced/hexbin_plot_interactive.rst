dataviz.bivariate.advanced.hexbin_plot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: hexbin_plot_interactive

Use case
--------

Use when a scatter plot of a large dataset overplots, to see point density as hexagonal bins.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.bivariate.advanced import hexbin_plot_interactive

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")

   fig = hexbin_plot_interactive(x, y)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/hexbin_plot_interactive.png" alt="hexbin_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
