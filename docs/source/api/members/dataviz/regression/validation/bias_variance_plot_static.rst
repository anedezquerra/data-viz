dataviz.regression.validation.bias_variance_plot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: bias_variance_plot_static

Use case
--------

Use to visualize the bias-variance trade-off across model complexity and locate the complexity that minimizes total error.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.validation import bias_variance_plot_static

   degree = np.arange(1, 11)
   bias_sq = 14.0 / degree ** 1.6
   variance = 0.35 * degree ** 1.8
   noise = np.full_like(degree, 4.0, dtype=float)

   ax = bias_variance_plot_static(
       degree, bias_sq, variance, noise=noise,
       title="Polynomial fit of compressor efficiency: bias-variance trade-off",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/bias_variance_plot_static.png" alt="bias_variance_plot_static example output"><figcaption>Example output</figcaption></figure></div>
