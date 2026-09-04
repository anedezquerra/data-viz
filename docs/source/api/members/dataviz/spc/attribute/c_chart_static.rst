dataviz.spc.attribute.c_chart_static
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: c_chart_static

Use case
--------

Use when counting defects per inspection unit of constant size, such as flaws per painted panel or solder defects per board.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import c_chart_static

   rng = np.random.default_rng(42)
   # Surface defects counted on 28 painted panels (constant inspection area)
   defects = rng.poisson(3.5, size=28)
   defects[21] = 14  # spray nozzle clog on panel 21

   ax = c_chart_static(defects, title="Painted Panels - Surface Defects per Panel")
   ax.set_xlabel("Panel")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/c_chart_static.png" alt="c_chart_static example output"><figcaption>Example output</figcaption></figure></div>
