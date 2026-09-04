dataviz.spc.attribute.g_chart_static
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: g_chart_static

Use case
--------

Use when monitoring opportunities or units produced between rare events, such as defects on a high-yield line.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import g_chart_static

   rng = np.random.default_rng(42)
   counts = rng.geometric(p=0.02, size=30)

   ax = g_chart_static(counts, title="Units between defects")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/g_chart_static.png" alt="g_chart_static example output"><figcaption>Example output</figcaption></figure></div>
