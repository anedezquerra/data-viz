dataviz.spc.charts.x_range_chart
================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.charts</p></div>

.. currentmodule:: dataviz.spc.charts

.. autofunction:: x_range_chart

Use case
--------

Use as the default static entry point for plotting individual values alongside their moving ranges when subgrouping is impractical.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.charts import x_range_chart

   rng = np.random.default_rng(42)
   # Shaft diameters (mm) sampled from a CNC lathe
   diameters = rng.normal(25.0, 0.08, size=30)
   diameters[19] = 25.42  # tool wear spike

   ax = x_range_chart(
       diameters, subgroup_size=5, title="Shaft Diameter X-Range Chart", ylabel="Diameter (mm)"
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/charts/x_range_chart.png" alt="x_range_chart example output"><figcaption>Example output</figcaption></figure></div>
