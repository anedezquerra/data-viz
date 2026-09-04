dataviz.spc.capability.CapabilityStats
======================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.spc.capability</p></div>

.. currentmodule:: dataviz.spc.capability

.. autoclass:: CapabilityStats
   :members:
   :show-inheritance:

Use case
--------

Carries sample size, mean, std, spec limits, Cp/Cpk, and PPM out-of-spec estimates; consumed when reporting whether a process meets customer specifications.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.spc.capability import CapabilityStats

   # Capability summary recorded for a 500 g filling process
   result = CapabilityStats(
       n=60,
       mean=500.1,
       std=1.2,
       lsl=497.0,
       usl=503.0,
       cp=0.833,
       cpk=0.806,
       ppm_below=0.0,
       ppm_above=0.0,
       ppm_below_normal=5123.4,
       ppm_above_normal=4012.6,
       ppm_total_normal=9136.0,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
