dataviz.spc.rules.individuals_limits
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autofunction:: individuals_limits

Use case
--------

Use to compute individuals chart limits from single observations via the moving-range sigma estimate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.rules import individuals_limits

   rng = np.random.default_rng(42)
   # Fill weights (g) from 30 consecutive bottles on a filling line
   weights = rng.normal(500.0, 1.1, size=30)
   weights[24] = 504.9  # overfill after valve wear

   result = individuals_limits(weights, sigma_multiplier=3.0)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
