dataviz.univariate.advanced.strip_plot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: strip_plot_interactive

Use case
--------

Use to display each observation as a jittered point, ideal for small samples where exact values and density matter.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.advanced import strip_plot_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   fig = strip_plot_interactive(values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/strip_plot_interactive.png" alt="strip_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
