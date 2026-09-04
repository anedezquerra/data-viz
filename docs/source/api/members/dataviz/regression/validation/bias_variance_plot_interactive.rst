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

   degree = np.arange(1, 11)
   bias_sq = 14.0 / degree ** 1.6
   variance = 0.35 * degree ** 1.8
   noise = np.full_like(degree, 4.0, dtype=float)

   fig = bias_variance_plot_interactive(
       degree, bias_sq, variance, noise=noise,
       title="Polynomial fit of compressor efficiency: bias-variance trade-off",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/bias_variance_plot_interactive.png" alt="bias_variance_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
