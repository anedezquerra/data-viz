dataviz.bivariate.advanced.density_contour_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: density_contour_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.bivariate.advanced import density_contour_interactive

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")

   fig = density_contour_interactive(x, y)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/density_contour_interactive.png" alt="density_contour_interactive example output"><figcaption>Example output</figcaption></figure></div>
