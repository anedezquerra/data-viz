dataviz.spc.variable.cusum_chart_static
=======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: cusum_chart_static

Use case
--------

Use to detect small persistent drifts in the process mean by accumulating deviations from target over time.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.variable import cusum_chart_static

   rng = np.random.default_rng(42)
   # Fill weights (g) with a small sustained shift that a Shewhart chart misses
   weights = rng.normal(500.0, 1.0, size=32)
   weights[22:] += 1.5  # slow valve drift shifts the mean

   ax = cusum_chart_static(
       weights, target=500.0, k=0.5, h=5.0, title="Fill Weight CUSUM Chart"
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/cusum_chart_static.png" alt="cusum_chart_static example output"><figcaption>Example output</figcaption></figure></div>
