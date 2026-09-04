dataviz.regression.transforms.power_transform_residual_panel_interactive
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.transforms</p></div>

.. currentmodule:: dataviz.regression.transforms

.. autofunction:: power_transform_residual_panel_interactive

Use case
--------

Compare residuals-vs-fitted for raw, log, and sqrt transforms side by side to choose the response transform that best stabilizes variance.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.transforms import power_transform_residual_panel_interactive

   rng = np.random.default_rng(42)
   n = 36
   y_pred = np.sort(rng.uniform(20, 400, n))              # fitted claim cost (k$)
   spread = 0.04 * y_pred                                 # heteroscedastic noise
   resid_orig = rng.normal(0, 1, n) * spread
   resid_log = rng.normal(0, 0.06, n)
   resid_sqrt = rng.normal(0, 0.35, n)

   fig = power_transform_residual_panel_interactive(
       y_pred, resid_orig, resid_log, resid_sqrt,
       title="Claim cost model: residual panel across power transforms",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/transforms/power_transform_residual_panel_interactive.png" alt="power_transform_residual_panel_interactive example output"><figcaption>Example output</figcaption></figure></div>
