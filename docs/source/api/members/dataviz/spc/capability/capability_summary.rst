dataviz.spc.capability.capability_summary
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.capability</p></div>

.. currentmodule:: dataviz.spc.capability

.. autofunction:: capability_summary

Use case
--------

Use to quantify whether a stable process meets specifications by computing Cp, Cpk, and PPM defect estimates against LSL/USL.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.capability import capability_summary

   rng = np.random.default_rng(42)
   # Fill weights (g) from a bottling line, spec 497-503 g
   weights = rng.normal(500.0, 1.2, size=60)
   weights[41] = 504.8  # overfilled bottle after valve wear

   result = capability_summary(weights, lsl=497.0, usl=503.0)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
