dataviz.spc.rules.RuleViolation
===============================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autoclass:: RuleViolation
   :members:
   :show-inheritance:

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.rules import RuleViolation

   result = RuleViolation(index=24, value=11.8, rule="beyond_limits", message="Point outside control limits")
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
