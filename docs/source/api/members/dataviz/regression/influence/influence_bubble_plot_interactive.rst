dataviz.regression.influence.influence_bubble_plot_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.influence</p></div>

.. currentmodule:: dataviz.regression.influence

.. autofunction:: influence_bubble_plot_interactive

Use case
--------

Use to view leverage and studentized residuals together, with bubble size encoding Cook's distance.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.influence import influence_bubble_plot_interactive

   rng = np.random.default_rng(42)
   n = 28
   ad_spend = rng.uniform(5.0, 60.0, n)
   store_traffic = rng.uniform(100.0, 900.0, n)
   X = pd.DataFrame({"ad_spend_kusd": ad_spend,
                      "store_traffic_daily": store_traffic})
   X.loc[27, "ad_spend_kusd"] = 95.0  # an outlier campaign week
   y = pd.Series(20.0 + 1.8 * ad_spend + 0.05 * store_traffic
                 + rng.normal(0.0, 6.0, n), name="weekly_revenue_kusd")
   y.iloc[27] = 260.0
   beta = np.linalg.lstsq(np.column_stack([np.ones(n), X]), y, rcond=None)[0]
   y_pred = np.column_stack([np.ones(n), X]) @ beta

   fig = influence_bubble_plot_interactive(
       X, y, y_pred, title="Marketing Mix Model: Influence Bubble Plot",
       colorscale="Viridis", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/influence/influence_bubble_plot_interactive.png" alt="influence_bubble_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
