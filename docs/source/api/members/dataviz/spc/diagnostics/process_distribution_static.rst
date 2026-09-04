dataviz.spc.diagnostics.process_distribution_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: process_distribution_static

Use case
--------

Use to check the shape, center, and sigma spread of process output with a histogram and sigma bands before assuming normality.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.diagnostics import process_distribution_static

   rng = np.random.default_rng(42)
   # Fill weights (g) collected during a capability study on line 3
   weights = rng.normal(500.0, 1.1, size=40)
   weights[33] = 504.6  # overfill after valve wear

   ax = process_distribution_static(weights, bins=15, title="Line 3 Fill Weight Distribution")
   ax.set_xlabel("Fill weight (g)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/process_distribution_static.png" alt="process_distribution_static example output"><figcaption>Example output</figcaption></figure></div>
