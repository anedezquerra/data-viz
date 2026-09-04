dataviz.spc.attribute.c_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: c_chart_interactive

Use case
--------

Use when counting defects per inspection unit of constant size, such as flaws per painted panel or solder defects per board.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import c_chart_interactive

   defects = np.array([8, 12, 9, 15, 7, 11, 10, 13, 8, 12])

   fig = c_chart_interactive(defects, title="Surface defects per panel")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/c_chart_interactive.png" alt="c_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
