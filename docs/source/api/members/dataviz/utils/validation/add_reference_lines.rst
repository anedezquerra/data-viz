dataviz.utils.validation.add_reference_lines
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.utils.validation</p></div>

.. currentmodule:: dataviz.utils.validation

.. autofunction:: add_reference_lines

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.utils.validation import add_reference_lines

   rng = np.random.default_rng(42)
   fig, ax = plt.subplots()
   ax.plot(np.arange(30), rng.normal(loc=10.0, scale=0.4, size=30))

   add_reference_lines(ax, hline=10.0, vline=15)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
