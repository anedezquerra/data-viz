dataviz.spc.x_range.x_range_chart_static
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.x_range</p></div>

.. currentmodule:: dataviz.spc.x_range

.. autofunction:: x_range_chart_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.x_range import x_range_chart_static

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   ax = x_range_chart_static(data, subgroup_size=5)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/x_range/x_range_chart_static.png" alt="x_range_chart_static example output"><figcaption>Example output</figcaption></figure></div>
