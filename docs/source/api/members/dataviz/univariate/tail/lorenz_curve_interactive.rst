dataviz.univariate.tail.lorenz_curve_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.tail</p></div>

.. currentmodule:: dataviz.univariate.tail

.. autofunction:: lorenz_curve_interactive

Use case
--------

Use to visualize inequality in non-negative values against the perfect-equality reference line.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.tail import lorenz_curve_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   fig = lorenz_curve_interactive(values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/tail/lorenz_curve_interactive.png" alt="lorenz_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
