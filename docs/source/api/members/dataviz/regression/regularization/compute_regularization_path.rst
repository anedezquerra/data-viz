dataviz.regression.regularization.compute_regularization_path
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.regularization</p></div>

.. currentmodule:: dataviz.regression.regularization

.. autofunction:: compute_regularization_path

Use case
--------

Use to compute lasso, ridge, or elastic-net coefficient paths over a grid of penalties before plotting them.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.regularization import compute_regularization_path

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

   alphas, coefs = compute_regularization_path(
       stores, weekly_sales, n_alphas=40, l1_ratio=1.0
   )
   result = {"alphas": np.round(alphas, 4), "coef_shape": coefs.shape}
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
