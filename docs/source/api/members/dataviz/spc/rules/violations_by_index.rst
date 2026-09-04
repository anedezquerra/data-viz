dataviz.spc.rules.violations_by_index
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autofunction:: violations_by_index

Use case
--------

Use to group detected rule violations by observation index when annotating multiple rules on a single chart point.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.rules import detect_rule_violations, violations_by_index

   rng = np.random.default_rng(42)
   # Coating thickness (microns) with a spike and a sustained shift
   thickness = rng.normal(100.0, 1.0, size=32)
   thickness[22] = 105.1  # spray gun surge beyond limits
   thickness[26:] += 2.5  # nozzle wear shifts the process mean

   violations = detect_rule_violations(thickness)
   result = violations_by_index(violations)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
