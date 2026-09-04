dataviz.univariate.violin_plot.violin_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.violin_plot</p></div>

.. currentmodule:: dataviz.univariate.violin_plot

.. autofunction:: violin_plot_interactive

Use case
--------

Use to show the full distribution shape with density width plus an inner box, revealing modality that a box plot hides.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.violin_plot import violin_plot_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   fig = violin_plot_interactive(values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/violin_plot/violin_plot_interactive.png" alt="violin_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
