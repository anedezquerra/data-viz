dataviz.spc.capability.CapabilityStats
======================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.spc.capability</p></div>

.. currentmodule:: dataviz.spc.capability

.. autoclass:: CapabilityStats
   :members:
   :show-inheritance:

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.capability import CapabilityStats

   result = CapabilityStats(n=30, mean=10.0, std=0.4, lsl=9.0, usl=11.0, cp=0.833, cpk=0.833, ppm_below=0.0, ppm_above=0.0, ppm_below_normal=6209.7, ppm_above_normal=6209.7, ppm_total_normal=12419.4)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
