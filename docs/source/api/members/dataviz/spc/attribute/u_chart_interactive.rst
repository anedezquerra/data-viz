dataviz.spc.attribute.u_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: u_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import u_chart_interactive

   defects = np.array([8, 12, 9, 15, 7, 11, 10, 13, 8, 12])
   units = np.array([40, 50, 45, 55, 42, 48, 50, 52, 44, 49])

   fig = u_chart_interactive(defects, units, title="Defects per inspected unit")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/spc/attribute/u_chart_interactive.png" alt="u_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
