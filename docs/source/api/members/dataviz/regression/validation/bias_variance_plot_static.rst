dataviz.regression.validation.bias_variance_plot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: bias_variance_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.validation import bias_variance_plot_static

   complexity = np.arange(1, 11)
   bias_squared = 0.5 / complexity
   variance = 0.002 * complexity**2
   noise = np.full(10, 0.05)

   ax = bias_variance_plot_static(complexity, bias_squared, variance, noise=noise)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/validation/bias_variance_plot_static.png" alt="bias_variance_plot_static example output"><figcaption>Example output</figcaption></figure></div>
