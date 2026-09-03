dataviz.regression.quantile.huber_vs_ols_overlay_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: huber_vs_ols_overlay_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.quantile import huber_vs_ols_overlay_static

   rng = np.random.default_rng(42)
   x = np.linspace(0.0, 10.0, 60)
   y = 2 * x + rng.normal(0.0, 1.0, size=60)
   y_ols = 2 * x + 0.1
   y_huber = 2 * x - 0.05

   ax = huber_vs_ols_overlay_static(x, y, y_ols, y_huber)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
