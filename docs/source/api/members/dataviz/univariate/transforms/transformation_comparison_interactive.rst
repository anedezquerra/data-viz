dataviz.univariate.transforms.transformation_comparison_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.transforms</p></div>

.. currentmodule:: dataviz.univariate.transforms

.. autofunction:: transformation_comparison_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.transforms import transformation_comparison_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   fig = transformation_comparison_interactive(values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/univariate/transforms/transformation_comparison_interactive.png" alt="transformation_comparison_interactive example output"><figcaption>Example output</figcaption></figure></div>
