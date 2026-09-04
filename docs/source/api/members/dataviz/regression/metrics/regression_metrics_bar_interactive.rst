dataviz.regression.metrics.regression_metrics_bar_interactive
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.metrics</p></div>

.. currentmodule:: dataviz.regression.metrics

.. autofunction:: regression_metrics_bar_interactive

Use case
--------

Use to summarize a single model's regression metrics side by side in a bar chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.metrics import regression_metrics_bar_interactive
   from dataviz.regression.helpers import compute_regression_metrics

   rng = np.random.default_rng(42)
   n = 30
   sqft = rng.uniform(900.0, 3500.0, n)
   y = pd.Series(60.0 + 0.16 * sqft + rng.normal(0.0, 12.0, n), name="price_kusd")
   pred_ols = pd.Series(60.0 + 0.16 * sqft + rng.normal(0.0, 8.0, n),
                        name="ols_pred")
   pred_ridge = pd.Series(62.0 + 0.15 * sqft + rng.normal(0.0, 10.0, n),
                          name="ridge_pred")
   pred_gbm = pd.Series(61.0 + 0.16 * sqft + rng.normal(0.0, 6.0, n),
                        name="gbm_pred")
   model_metrics = {
       "OLS": compute_regression_metrics(y, pred_ols).as_dict(),
       "Ridge": compute_regression_metrics(y, pred_ridge).as_dict(),
       "GBM": compute_regression_metrics(y, pred_gbm).as_dict(),
   }

   fig = regression_metrics_bar_interactive(
       y, pred_gbm, metrics=("mae", "rmse", "medae", "r2"),
       title="Housing Price GBM: Test Metrics", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/metrics/regression_metrics_bar_interactive.png" alt="regression_metrics_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
