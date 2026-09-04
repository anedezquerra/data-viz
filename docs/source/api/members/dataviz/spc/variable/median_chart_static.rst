dataviz.spc.variable.median_chart_static
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: median_chart_static

Use case
--------

Use when monitoring subgrouped measurements by subgroup median, a robust X-tilde alternative when outliers skew the mean.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.variable import median_chart_static

   rng = np.random.default_rng(42)
   # Hardness readings (HRC): 24 subgroups of 5 parts from heat treatment
   hardness = rng.normal(58.0, 1.2, size=120)
   hardness[75:80] -= 3.5  # quench-tank temperature drop in subgroup 15

   ax = median_chart_static(hardness, subgroup_size=5, title="Part Hardness Median Chart")
   ax.set_ylabel("Subgroup median (HRC)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/median_chart_static.png" alt="median_chart_static example output"><figcaption>Example output</figcaption></figure></div>
