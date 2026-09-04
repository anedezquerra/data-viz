dataviz.spc.capability.capability_histogram_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.capability</p></div>

.. currentmodule:: dataviz.spc.capability

.. autofunction:: capability_histogram_static

Use case
--------

Use to show a process histogram against specification limits with a fitted normal curve, for capability reviews with customers or auditors.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.capability import capability_histogram_static

   rng = np.random.default_rng(42)
   # Fill weights (g) from a bottling line, spec 497-503 g
   weights = rng.normal(500.0, 1.2, size=60)
   weights[41] = 504.8  # overfilled bottle after valve wear

   ax = capability_histogram_static(
       weights, lsl=497.0, usl=503.0, bins=20, title="Fill Weight Capability"
   )
   ax.set_xlabel("Fill weight (g)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/capability/capability_histogram_static.png" alt="capability_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
