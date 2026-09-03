dataviz.univariate.histogram.histogram_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.histogram</p></div>

.. currentmodule:: dataviz.univariate.histogram

.. autofunction:: histogram_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.histogram import histogram_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   fig = histogram_interactive(values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/univariate/histogram/histogram_interactive.png" alt="histogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
