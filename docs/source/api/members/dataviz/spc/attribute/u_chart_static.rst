dataviz.spc.attribute.u_chart_static
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: u_chart_static

Use case
--------

Use when tracking defects per unit across samples of varying size, such as scratches per square meter of rolled sheet.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import u_chart_static

   rng = np.random.default_rng(42)
   # Defects per fabric roll with varying roll lengths
   units = rng.integers(8, 16, size=30)
   defects = rng.poisson(units * 0.4)
   defects[22] = 18  # loom tension fault on roll 22

   ax = u_chart_static(defects, units, title="Fabric Rolls - Defects per Unit")
   ax.set_xlabel("Roll")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/u_chart_static.png" alt="u_chart_static example output"><figcaption>Example output</figcaption></figure></div>
