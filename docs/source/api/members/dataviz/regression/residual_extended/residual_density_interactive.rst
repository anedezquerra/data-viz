dataviz.regression.residual_extended.residual_density_interactive
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: residual_density_interactive

Use case
--------

Use to assess the shape of the residual distribution with a smooth kernel-density estimate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.residual_extended import residual_density_interactive

   rng = np.random.default_rng(42)
   flights = pd.Series(np.arange(1, 51), name="flight")
   actual_delay = pd.Series(rng.normal(12, 18, 50).round(1), name="actual_delay_min")
   predicted_delay = pd.Series(
       actual_delay + rng.laplace(0, 6, 50), name="predicted_delay_min"
   )

   fig = residual_density_interactive(
       actual_delay, predicted_delay, bandwidth=4.0,
       title="Flight delay model: residual kernel density",
       color="#6a4c93", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/residual_density_interactive.png" alt="residual_density_interactive example output"><figcaption>Example output</figcaption></figure></div>
