dataviz.regression.residual.residual_plot_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual</p></div>

.. currentmodule:: dataviz.regression.residual

.. autofunction:: residual_plot_interactive

Use case
--------

Use as the first residual diagnostic: plot residuals vs fitted values to reveal nonlinearity or heteroscedasticity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.residual import residual_plot_interactive

   rng = np.random.default_rng(42)
   homes = pd.Series(np.arange(1, 23), name="listing")
   actual_price = pd.Series(
       rng.uniform(180, 850, 22).round(0), name="actual_price_kusd"
   )
   predicted_price = pd.Series(
       actual_price + rng.normal(0, 32, 22) + 0.05 * (actual_price - 500),
       name="predicted_price_kusd",
   )

   fig = residual_plot_interactive(
       actual_price, predicted_price,
       title="Home appraisal model: residual diagnostics",
       marker_color="#2a6f97", marker_size=10,
       line_color="#d62728", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual/residual_plot_interactive.png" alt="residual_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
