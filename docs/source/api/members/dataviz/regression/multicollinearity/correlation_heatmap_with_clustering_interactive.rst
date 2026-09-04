dataviz.regression.multicollinearity.correlation_heatmap_with_clustering_interactive
====================================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: correlation_heatmap_with_clustering_interactive

Use case
--------

Use to surface clusters of highly correlated predictors so redundant features can be dropped or combined.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.multicollinearity import correlation_heatmap_with_clustering_interactive

   rng = np.random.default_rng(42)
   n = 48
   ad_spend = rng.normal(50, 12, n)
   marketing = pd.DataFrame({
       "tv_spend_k": ad_spend + rng.normal(0, 4, n),
       "radio_spend_k": 0.6 * ad_spend + rng.normal(0, 6, n),
       "social_spend_k": rng.normal(20, 6, n),
       "email_campaigns": rng.integers(1, 9, n).astype(float),
       "web_traffic_k": 1.4 * ad_spend + rng.normal(0, 10, n),
   })

   fig = correlation_heatmap_with_clustering_interactive(
       marketing, feature_names=list(marketing.columns),
       title="Marketing mix model: clustered predictor correlations",
       colorscale="RdBu", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/correlation_heatmap_with_clustering_interactive.png" alt="correlation_heatmap_with_clustering_interactive example output"><figcaption>Example output</figcaption></figure></div>
