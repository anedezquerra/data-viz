dataviz.regression.quantile.quantile_loss_curve_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: quantile_loss_curve_interactive

Use case
--------

Use to compare pinball loss across quantile levels when selecting or evaluating quantile-regression models.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.quantile import quantile_loss_curve_interactive

   rng = np.random.default_rng(42)
   quantiles = pd.Series(np.round(np.arange(0.05, 0.96, 0.05), 2), name="tau")
   residual_sample = rng.normal(0, 2.5, 400)
   losses = pd.Series(
       [np.mean(np.maximum(t * residual_sample, (t - 1) * residual_sample))
        for t in quantiles],
       name="pinball_loss",
   )

   fig = quantile_loss_curve_interactive(
       quantiles, losses,
       title="Demand forecasting: pinball loss by quantile level",
       color="#6a4c93", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/quantile/quantile_loss_curve_interactive.png" alt="quantile_loss_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
