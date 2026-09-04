dataviz.spc.attribute.laney_u_chart_static
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: laney_u_chart_static

Use case
--------

Use when a u chart shows over-dispersion from large or varying areas of opportunity; the Laney u' chart widens limits to match actual variation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import laney_u_chart_static

   rng = np.random.default_rng(42)
   # Cable defects per unit with varying production volumes and overdispersion
   units = rng.integers(20, 60, size=28)
   defects = rng.poisson(units * 0.6)
   defects[20] = 70  # extruder contamination event

   ax = laney_u_chart_static(defects, units, title="Cable Production - Defects per Unit (Laney u-prime)")
   ax.set_xlabel("Batch")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/laney_u_chart_static.png" alt="laney_u_chart_static example output"><figcaption>Example output</figcaption></figure></div>
