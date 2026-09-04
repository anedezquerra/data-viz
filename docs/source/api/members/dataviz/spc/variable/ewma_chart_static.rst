dataviz.spc.variable.ewma_chart_static
======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: ewma_chart_static

Use case
--------

Use to detect small sustained shifts in the process mean earlier than a Shewhart chart by weighting recent observations more heavily.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.variable import ewma_chart_static

   rng = np.random.default_rng(42)
   # Film thickness (mm) with a slow drift from die-lip buildup
   thickness = rng.normal(2.0, 0.02, size=32)
   thickness[20:] += np.linspace(0.0, 0.06, 12)  # gradual drift

   ax = ewma_chart_static(thickness, lambda_=0.25, title="Film Thickness EWMA Chart")
   ax.set_ylabel("Thickness (mm)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/ewma_chart_static.png" alt="ewma_chart_static example output"><figcaption>Example output</figcaption></figure></div>
