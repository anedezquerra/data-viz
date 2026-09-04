dataviz.spc.capability.capability_histogram_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.capability</p></div>

.. currentmodule:: dataviz.spc.capability

.. autofunction:: capability_histogram_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.capability import capability_histogram_static

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   ax = capability_histogram_static(data, lsl=9.0, usl=11.0, bins=12)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/spc/capability/capability_histogram_static.png" alt="capability_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
