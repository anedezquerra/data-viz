dataviz.spc.dashboard.spc_dashboard_static
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.dashboard</p></div>

.. currentmodule:: dataviz.spc.dashboard

.. autofunction:: spc_dashboard_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.dashboard import spc_dashboard_static

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   fig = spc_dashboard_static(data, bins=12, title="Filling process overview")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/dashboard/spc_dashboard_static.png" alt="spc_dashboard_static example output"><figcaption>Example output</figcaption></figure></div>
