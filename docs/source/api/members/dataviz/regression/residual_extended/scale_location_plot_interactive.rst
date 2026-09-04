dataviz.regression.residual_extended.scale_location_plot_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: scale_location_plot_interactive

Use case
--------

Use to check homoscedasticity by plotting sqrt of absolute standardized residuals against fitted values.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.residual_extended import scale_location_plot_interactive

   rng = np.random.default_rng(42)
   orders = pd.Series(np.arange(1, 46), name="order")
   actual_cost = pd.Series(
       rng.uniform(20, 400, 45).round(1), name="actual_cost_usd"
   )
   hetero_noise = rng.normal(0, 1, 45) * (4 + 0.05 * actual_cost)
   predicted_cost = pd.Series(actual_cost + hetero_noise, name="predicted_cost_usd")

   fig = scale_location_plot_interactive(
       actual_cost, predicted_cost,
       title="Shipping cost model: scale-location check",
       color="#4878d0", trend_color="#d62728", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/scale_location_plot_interactive.png" alt="scale_location_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
