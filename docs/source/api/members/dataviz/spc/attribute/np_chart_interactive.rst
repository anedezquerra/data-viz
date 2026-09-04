dataviz.spc.attribute.np_chart_interactive
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: np_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import np_chart_interactive

   defects = np.array([3, 5, 4, 6, 2, 7, 4, 5, 3, 6])

   fig = np_chart_interactive(defects, sample_size=100, title="Defectives per lot")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/np_chart_interactive.png" alt="np_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
