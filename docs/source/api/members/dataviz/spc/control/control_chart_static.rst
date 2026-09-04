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
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   ax = control_chart_static(data, title="Filling process", ylabel="Fill weight (g)")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/control/control_chart_static.png" alt="control_chart_static example output"><figcaption>Example output</figcaption></figure></div>
