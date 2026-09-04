dataviz.regression.comparison.residual_density_overlay_multi_interactive
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: residual_density_overlay_multi_interactive

Use case
--------

Use to compare residual distributions across models; tighter, zero-centered KDEs indicate better calibrated errors.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.comparison import residual_density_overlay_multi_interactive

   rng = np.random.default_rng(42)
   residuals = [rng.normal(0, 5, 40),
                rng.normal(0.5, 8, 40),
                rng.normal(-1.5, 12, 40)]
   labels = ["Ridge", "SVR", "KNN"]

   fig = residual_density_overlay_multi_interactive(
       residuals, labels,
       title="Energy Demand Models: Residual Density Overlay",
       template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/residual_density_overlay_multi_interactive.png" alt="residual_density_overlay_multi_interactive example output"><figcaption>Example output</figcaption></figure></div>
