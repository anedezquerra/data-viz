dataviz.spc.rules.xbar_r_limits
===============================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autofunction:: xbar_r_limits

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.rules import xbar_r_limits

   rng = np.random.default_rng(42)
   data = rng.normal(loc=10.0, scale=0.35, size=(20, 5))

   x_limits, r_limits, means, ranges = xbar_r_limits(data)
   print(x_limits)
   print(r_limits)
   print(means.head())

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
