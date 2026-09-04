dataviz.spc.charts.control_chart
================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.charts</p></div>

.. currentmodule:: dataviz.spc.charts

.. autofunction:: control_chart

Use case
--------

Use as the default static control chart entry point when plotting process observations against computed control limits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.charts import control_chart

   rng = np.random.default_rng(42)
   # Oven temperature (deg C) logged every 15 minutes over one shift
   temps = rng.normal(180.0, 1.5, size=30)
   temps[22] = 186.4  # heating element surge

   ax = control_chart(temps, title="Oven Temperature Control Chart", ylabel="Temperature (deg C)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/charts/control_chart.png" alt="control_chart example output"><figcaption>Example output</figcaption></figure></div>
