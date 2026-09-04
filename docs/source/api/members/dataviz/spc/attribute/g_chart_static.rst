dataviz.spc.attribute.g_chart_static
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: g_chart_static

Use case
--------

Use when monitoring opportunities or units produced between rare events, such as defects on a high-yield line.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import g_chart_static

   rng = np.random.default_rng(42)
   # Units produced between rare contamination events on a filling line
   counts = rng.geometric(p=0.03, size=25)
   counts[15] = 160  # unusually long clean run after filter upgrade

   ax = g_chart_static(counts, title="Contamination Events - Units Between Occurrences")
   ax.set_xlabel("Event Number")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/g_chart_static.png" alt="g_chart_static example output"><figcaption>Example output</figcaption></figure></div>
