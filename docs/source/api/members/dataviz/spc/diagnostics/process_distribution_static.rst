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
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   ax = process_distribution_static(data, bins=12)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/process_distribution_static.png" alt="process_distribution_static example output"><figcaption>Example output</figcaption></figure></div>
