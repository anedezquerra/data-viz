dataviz.spc.attribute.np_chart_static
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: np_chart_static

Use case
--------

Use when counting defective units per lot of constant size, such as daily rejected parts from a fixed production batch.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import np_chart_static

   rng = np.random.default_rng(42)
   # 28 incoming lots, 200 parts inspected from each lot
   defects = rng.binomial(200, 0.04, size=28)
   defects[19] = 19  # lot from a new supplier runs high

   ax = np_chart_static(defects, sample_size=200, title="Incoming Inspection - Defective Parts per Lot")
   ax.set_xlabel("Lot")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/np_chart_static.png" alt="np_chart_static example output"><figcaption>Example output</figcaption></figure></div>
