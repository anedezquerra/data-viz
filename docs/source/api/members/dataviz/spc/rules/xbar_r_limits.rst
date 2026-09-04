dataviz.spc.rules.xbar_r_limits
===============================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autofunction:: xbar_r_limits

Use case
--------

Use to compute Xbar and R chart limits for small subgroups, typically size 2 to 10, using the average range.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.rules import xbar_r_limits

   rng = np.random.default_rng(42)
   # Shaft diameters (mm): 25 subgroups of 5 parts from a CNC lathe
   diameters = rng.normal(25.0, 0.08, size=125)
   diameters[100:105] += 0.25  # tool wear shift in subgroup 20

   result = xbar_r_limits(diameters, subgroup_size=5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
