dataviz.core.plot
=================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.core</p></div>

.. currentmodule:: dataviz.core

.. autofunction:: plot

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.core import plot

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = plot(values)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../_static/api/dataviz/core/plot.png" alt="plot example output"><figcaption>Example output</figcaption></figure></div>
