dataviz.spc.x_range.x_range_chart_static
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.x_range</p></div>

.. currentmodule:: dataviz.spc.x_range

.. autofunction:: x_range_chart_static

Use case
--------

Use to plot individual values with their moving ranges for processes measured one part at a time.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.x_range import x_range_chart_static

   rng = np.random.default_rng(42)
   # Shaft diameters (mm) sampled from a CNC lathe
   diameters = rng.normal(25.0, 0.08, size=30)
   diameters[19] = 25.42  # tool wear spike

   ax = x_range_chart_static(
       diameters, subgroup_size=5, title="Shaft Diameter X-Range Chart", ylabel="Diameter (mm)"
   )
   ax.set_xlabel("Sample")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/x_range/x_range_chart_static.png" alt="x_range_chart_static example output"><figcaption>Example output</figcaption></figure></div>
