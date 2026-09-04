dataviz.regression.regularization.lasso_path_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.regularization</p></div>

.. currentmodule:: dataviz.regression.regularization

.. autofunction:: lasso_path_static

Use case
--------

Use to see which coefficients shrink to zero as the lasso penalty grows, guiding feature selection.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.regularization import lasso_path_static

   rng = np.random.default_rng(42)
   n = 30
   promo = rng.uniform(0, 10, n)
   stores = pd.DataFrame({
       "price_index": rng.normal(100, 8, n),
       "promo_depth_pct": promo,
       "shelf_share_pct": 30 + 2 * promo + rng.normal(0, 3, n),
       "competitor_dist_km": rng.uniform(0.2, 12, n),
       "foot_traffic_k": rng.normal(4.5, 1.2, n),
       "online_ads_k": rng.normal(1.8, 0.7, n),
   })
   weekly_sales = pd.Series(
       120 - 1.1 * stores["price_index"] + 6.0 * promo
       + 2.5 * stores["foot_traffic_k"] + rng.normal(0, 9, n),
       name="weekly_sales_k",
   )

   ax = lasso_path_static(
       stores, weekly_sales, feature_names=list(stores.columns), n_alphas=40,
       title="Retail sales drivers: lasso coefficient path",
       cmap="tab10", theme="minimal",
   )
   ax.set_ylabel("Coefficient (kUSD per unit)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/regularization/lasso_path_static.png" alt="lasso_path_static example output"><figcaption>Example output</figcaption></figure></div>
