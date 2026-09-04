dataviz.spc.attribute.laney_u_chart_interactive
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: laney_u_chart_interactive

Use case
--------

Use when a u chart shows over-dispersion from large or varying areas of opportunity; the Laney u' chart widens limits to match actual variation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.spc.attribute import laney_u_chart_interactive

   defects = pd.Series([2, 1, 3, 0, 2, 1])
   units = pd.Series([50, 48, 52, 51, 50, 49])

   fig = laney_u_chart_interactive(defects, units)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/laney_u_chart_interactive.png" alt="laney_u_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
