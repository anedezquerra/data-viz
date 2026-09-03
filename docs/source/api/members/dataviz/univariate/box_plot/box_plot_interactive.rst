dataviz.univariate.box_plot.box_plot_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.box_plot</p></div>

.. currentmodule:: dataviz.univariate.box_plot

.. autofunction:: box_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.box_plot import box_plot_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   fig = box_plot_interactive(values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/univariate/box_plot/box_plot_interactive.png" alt="box_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
