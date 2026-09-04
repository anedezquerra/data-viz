dataviz.spc.control.control_chart_static
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.control</p></div>

.. currentmodule:: dataviz.spc.control

.. autofunction:: control_chart_static

Use case
--------

Use to plot process observations against computed control limits to judge whether a process is in statistical control.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.control import control_chart_static

   rng = np.random.default_rng(42)
   # Oven temperature (deg C) logged every 15 minutes over one shift
   temps = rng.normal(180.0, 1.5, size=30)
   temps[22] = 186.4  # heating element surge

   ax = control_chart_static(
       temps,
       title="Oven Temperature Control Chart",
       ylabel="Temperature (deg C)",
       sigma_multiplier=3.0,
       color_data="navy",
       marker_size=5,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/control/control_chart_static.png" alt="control_chart_static example output"><figcaption>Example output</figcaption></figure></div>
