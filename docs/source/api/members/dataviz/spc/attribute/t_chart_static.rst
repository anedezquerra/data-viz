dataviz.spc.attribute.t_chart_static
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: t_chart_static

Use case
--------

Use when monitoring elapsed time between rare events, such as hours between equipment failures or safety incidents.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import t_chart_static

   rng = np.random.default_rng(42)
   # Hours between recordable safety incidents across a plant
   times = rng.exponential(scale=12.0, size=25)
   times[14] = 85.0  # long incident-free stretch after retraining

   ax = t_chart_static(times, title="Safety Incidents - Hours Between Events")
   ax.set_xlabel("Event Number")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/t_chart_static.png" alt="t_chart_static example output"><figcaption>Example output</figcaption></figure></div>
