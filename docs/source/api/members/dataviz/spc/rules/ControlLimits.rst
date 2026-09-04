dataviz.spc.rules.ControlLimits
===============================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autoclass:: ControlLimits
   :members:
   :show-inheritance:

Use case
--------

Carries center line, lower/upper limits, and sigma estimate for a control chart; consumed by charting and rule-detection functions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.spc.rules import ControlLimits

   # Individuals-chart limits for a 500 g filling process
   result = ControlLimits(center=500.2, lower=497.1, upper=503.3, sigma=1.03)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
