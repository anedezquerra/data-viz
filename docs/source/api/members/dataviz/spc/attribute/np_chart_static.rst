dataviz.spc.attribute.np_chart_static
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: np_chart_static

Use case
--------

Use when counting defective units per lot of constant size, such as daily rejected parts from a fixed production batch.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import np_chart_static

   defects = np.array([3, 5, 4, 6, 2, 7, 4, 5, 3, 6])

   ax = np_chart_static(defects, sample_size=100, title="Defectives per lot")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/np_chart_static.png" alt="np_chart_static example output"><figcaption>Example output</figcaption></figure></div>
