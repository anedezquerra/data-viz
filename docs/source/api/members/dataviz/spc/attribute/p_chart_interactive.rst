dataviz.spc.attribute.p_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: p_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import p_chart_interactive

   defects = np.array([3, 5, 4, 6, 2, 7, 4, 5, 3, 6])
   sample_sizes = np.array([100, 105, 98, 110, 102, 108, 100, 104, 99, 106])

   fig = p_chart_interactive(defects, sample_sizes, title="Supplier defect proportion")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/p_chart_interactive.png" alt="p_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
