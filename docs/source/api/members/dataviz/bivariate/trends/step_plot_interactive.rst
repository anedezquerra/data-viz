dataviz.bivariate.trends.step_plot_interactive
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.trends</p></div>

.. currentmodule:: dataviz.bivariate.trends

.. autofunction:: step_plot_interactive

Use case
--------

Use for values that change discretely at known points, such as cumulative counts or rate changes over time.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.bivariate.trends import step_plot_interactive

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")

   fig = step_plot_interactive(x, y)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/trends/step_plot_interactive.png" alt="step_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
