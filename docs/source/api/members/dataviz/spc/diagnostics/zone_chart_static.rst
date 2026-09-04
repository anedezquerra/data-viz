dataviz.spc.diagnostics.zone_chart_static
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: zone_chart_static

Use case
--------

Use to score points by sigma zone (1, 2, and 3 sigma bands) as a simple alternative to full run-rule control charts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.diagnostics import zone_chart_static

   rng = np.random.default_rng(42)
   # Reactor temperature (deg C) sampled hourly with a slow upward drift
   temps = rng.normal(85.0, 0.8, size=30)
   temps[22:] += np.linspace(0.0, 1.8, 8)  # fouling heat exchanger

   ax = zone_chart_static(temps, title="Reactor Temperature Zone Chart")
   ax.set_ylabel("Temperature (deg C)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/zone_chart_static.png" alt="zone_chart_static example output"><figcaption>Example output</figcaption></figure></div>
