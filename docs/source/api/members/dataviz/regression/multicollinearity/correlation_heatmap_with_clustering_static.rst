dataviz.regression.multicollinearity.correlation_heatmap_with_clustering_static
===============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: correlation_heatmap_with_clustering_static

Use case
--------

Use to surface clusters of highly correlated predictors so redundant features can be dropped or combined.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.multicollinearity import correlation_heatmap_with_clustering_static

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

   ax = correlation_heatmap_with_clustering_static(
       marketing, feature_names=list(marketing.columns),
       title="Marketing mix model: clustered predictor correlations",
       cmap="RdBu_r", theme="minimal",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/correlation_heatmap_with_clustering_static.png" alt="correlation_heatmap_with_clustering_static example output"><figcaption>Example output</figcaption></figure></div>
