dataviz.spc.rules.subgroup_matrix
=================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autofunction:: subgroup_matrix

Use case
--------

Use to reshape raw or grouped observations into a subgroup matrix before computing Xbar-R or Xbar-S limits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.rules import subgroup_matrix

   rng = np.random.default_rng(42)
   # Torque readings (N m) from 25 subgroups of 5 fasteners each
   torque = rng.normal(18.0, 0.6, size=125)

   result = subgroup_matrix(torque, subgroup_size=5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
