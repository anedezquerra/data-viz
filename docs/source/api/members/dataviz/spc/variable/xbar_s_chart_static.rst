dataviz.spc.variable.xbar_s_chart_static
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: xbar_s_chart_static

Use case
--------

Use when monitoring larger subgroups where the standard deviation tracks within-subgroup spread more precisely than the range.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.variable import xbar_s_chart_static

   rng = np.random.default_rng(42)
   # Viscosity readings (cP): 22 subgroups of 6 samples per batch
   viscosity = rng.normal(350.0, 4.0, size=132)
   viscosity[90:96] += 14.0  # raw-material change in subgroup 15

   ax_xbar, ax_s = xbar_s_chart_static(
       viscosity, subgroup_size=6, title="Batch Viscosity Xbar-S Chart"
   )
   ax_xbar.set_ylabel("Subgroup mean (cP)")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/xbar_s_chart_static.png" alt="xbar_s_chart_static example output"><figcaption>Example output</figcaption></figure></div>
