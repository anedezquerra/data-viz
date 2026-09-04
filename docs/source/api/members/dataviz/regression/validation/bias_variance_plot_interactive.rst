dataviz.regression.validation.bias_variance_plot_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: bias_variance_plot_interactive

Use case
--------

Use to visualize the bias-variance trade-off across model complexity and locate the complexity that minimizes total error.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.validation import bias_variance_plot_interactive

   complexity = np.arange(1, 11)
   bias_squared = 0.5 / complexity
   variance = 0.002 * complexity**2
   noise = np.full(10, 0.05)

   fig = bias_variance_plot_interactive(complexity, bias_squared, variance, noise=noise)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/bias_variance_plot_interactive.png" alt="bias_variance_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
