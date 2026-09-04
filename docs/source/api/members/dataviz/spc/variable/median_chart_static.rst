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
   data = rng.normal(loc=10.0, scale=0.4, size=30)

   ax = median_chart_static(data, subgroup_size=5, title="Filling process")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/median_chart_static.png" alt="median_chart_static example output"><figcaption>Example output</figcaption></figure></div>
