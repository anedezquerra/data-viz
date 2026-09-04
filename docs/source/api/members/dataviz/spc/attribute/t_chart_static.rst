dataviz.spc.attribute.t_chart_static
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: t_chart_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import t_chart_static

   rng = np.random.default_rng(42)
   times = rng.exponential(scale=2.0, size=30)

   ax = t_chart_static(times, title="Hours between failures")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/t_chart_static.png" alt="t_chart_static example output"><figcaption>Example output</figcaption></figure></div>
