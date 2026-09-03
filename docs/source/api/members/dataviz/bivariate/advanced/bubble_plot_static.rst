dataviz.bivariate.advanced.bubble_plot_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: bubble_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.bivariate.advanced import bubble_plot_static

   rng = np.random.default_rng(42)
   x = rng.normal(loc=10.0, scale=2.0, size=30)
   y = 2.0 * x + rng.normal(loc=0.0, scale=1.0, size=30)
   size = rng.uniform(low=10.0, high=100.0, size=30)

   ax = bubble_plot_static(x, y, size, title="Bubble plot")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
