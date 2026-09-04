dataviz.spc.rules.xbar_s_limits
===============================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autofunction:: xbar_s_limits

Use case
--------

Use to compute Xbar and S chart limits for larger subgroups where the standard deviation estimates spread better than the range.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.rules import xbar_s_limits

   rng = np.random.default_rng(42)
   # Viscosity readings (cP): 22 subgroups of 6 samples per batch
   viscosity = rng.normal(350.0, 4.0, size=132)
   viscosity[90:96] += 14.0  # raw-material change in subgroup 15

   result = xbar_s_limits(viscosity, subgroup_size=6)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
