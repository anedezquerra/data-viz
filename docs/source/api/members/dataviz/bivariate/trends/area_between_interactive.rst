dataviz.bivariate.trends.area_between_interactive
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.trends</p></div>

.. currentmodule:: dataviz.bivariate.trends

.. autofunction:: area_between_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.bivariate.trends import area_between_interactive

   x = np.arange(30)
   y_lower = np.sin(x / 5.0)
   y_upper = y_lower + 0.5

   fig = area_between_interactive(x, y_lower, y_upper, title="Tolerance band")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/bivariate/trends/area_between_interactive.png" alt="area_between_interactive example output"><figcaption>Example output</figcaption></figure></div>
