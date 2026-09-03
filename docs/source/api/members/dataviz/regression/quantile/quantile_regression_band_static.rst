dataviz.regression.quantile.quantile_regression_band_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: quantile_regression_band_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.quantile import quantile_regression_band_static

   rng = np.random.default_rng(42)
   x = np.linspace(0.0, 10.0, 60)
   y = 2 * x + rng.normal(0.0, 1.0, size=60)
   y_low = 2 * x - 1.5
   y_med = 2 * x
   y_high = 2 * x + 1.5

   ax = quantile_regression_band_static(x, y, y_low, y_med, y_high)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
