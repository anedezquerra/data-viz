dataviz.spc.diagnostics.process_distribution_interactive
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.diagnostics</p></div>

.. currentmodule:: dataviz.spc.diagnostics

.. autofunction:: process_distribution_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.diagnostics import process_distribution_interactive

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.4, size=30)
   data[24] = 11.8  # Deliberate special-cause signal

   fig = process_distribution_interactive(data, bins=12)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/diagnostics/process_distribution_interactive.png" alt="process_distribution_interactive example output"><figcaption>Example output</figcaption></figure></div>
