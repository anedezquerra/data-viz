dataviz.spc.rules.detect_rule_violations
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autofunction:: detect_rule_violations

Use case
--------

Use to flag Western Electric and Nelson rule violations, such as runs and trends, on a series of process observations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.rules import detect_rule_violations

   rng = np.random.default_rng(42)
   # Coating thickness (microns) with a spike and a sustained shift
   thickness = rng.normal(100.0, 1.0, size=32)
   thickness[22] = 105.1  # spray gun surge beyond limits
   thickness[26:] += 2.5  # nozzle wear shifts the process mean

   result = detect_rule_violations(thickness, run_length=8, trend_length=6)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
