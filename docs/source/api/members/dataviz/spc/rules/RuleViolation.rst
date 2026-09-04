dataviz.spc.rules.RuleViolation
===============================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autoclass:: RuleViolation
   :members:
   :show-inheritance:

Use case
--------

Carries the observation index, value, violated rule name, and a message for one detected violation; consumed when annotating or grouping rule failures.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.spc.rules import RuleViolation

   # Violation logged when shift 24 exceeded the upper control limit
   result = RuleViolation(
       index=24, value=508.7, rule="beyond_limits", message="Point outside control limits"
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
