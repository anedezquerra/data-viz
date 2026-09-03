dataviz.spc.attribute.c_chart_static
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: c_chart_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import c_chart_static

   defects = np.array([8, 12, 9, 15, 7, 11, 10, 13, 8, 12])

   ax = c_chart_static(defects, title="Surface defects per panel")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/spc/attribute/c_chart_static.png" alt="c_chart_static example output"><figcaption>Example output</figcaption></figure></div>
