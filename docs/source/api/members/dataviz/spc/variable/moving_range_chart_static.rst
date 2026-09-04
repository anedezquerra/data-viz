dataviz.spc.variable.moving_range_chart_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: moving_range_chart_static

Use case
--------

Use to monitor short-term variation between consecutive individual measurements, companion to an individuals chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.variable import moving_range_chart_static

   rng = np.random.default_rng(42)
   # Fill weights (g) from 30 consecutive bottles on a filling line
   weights = rng.normal(500.0, 1.1, size=30)
   weights[24] = 504.9  # overfill after valve wear

   ax = moving_range_chart_static(weights, span=2, title="Fill Weight Moving Range")
   ax.set_ylabel("Moving range (g)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/moving_range_chart_static.png" alt="moving_range_chart_static example output"><figcaption>Example output</figcaption></figure></div>
