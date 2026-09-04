dataviz.bivariate.categorical.box_by_category_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: box_by_category_interactive

Use case
--------

Use to compare the spread, median, and outliers of a numeric variable across categories.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.bivariate.categorical import box_by_category_interactive

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")
   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")
   categories = pd.Series(["low", "medium", "high", "medium", "low"], name="Priority")

   fig = box_by_category_interactive(categories, values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/box_by_category_interactive.png" alt="box_by_category_interactive example output"><figcaption>Example output</figcaption></figure></div>
