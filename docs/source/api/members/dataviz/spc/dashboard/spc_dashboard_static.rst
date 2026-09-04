dataviz.spc.dashboard.spc_dashboard_static
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.dashboard</p></div>

.. currentmodule:: dataviz.spc.dashboard

.. autofunction:: spc_dashboard_static

Use case
--------

Use to review control, range, distribution, and rule-violation panels together for a compact daily process health check.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.dashboard import spc_dashboard_static

   rng = np.random.default_rng(42)
   # Moisture content (%) of granola batches across 36 production runs
   moisture = rng.normal(12.0, 0.3, size=36)
   moisture[26] = 13.4  # dryer malfunction on run 26

   fig = spc_dashboard_static(
       moisture, span=2, bins=15, title="Granola Moisture Content - SPC Dashboard"
   )
   fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/dashboard/spc_dashboard_static.png" alt="spc_dashboard_static example output"><figcaption>Example output</figcaption></figure></div>
