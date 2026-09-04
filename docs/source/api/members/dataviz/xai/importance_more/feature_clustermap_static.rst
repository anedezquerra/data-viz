dataviz.xai.importance_more.feature_clustermap_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: feature_clustermap_static

Use case
--------

Use to group features that share an importance signature across models or folds, revealing redundant or cohort-specific signals.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.importance_more import feature_clustermap_static

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "loan_amount", "annual_income",
       "employment_years", "num_open_accounts", "age", "num_credit_cards",
   ]
   latent = np.array([0.40, 0.38, 0.25, 0.23, 0.18, 0.10, 0.09, 0.07])
   folds = [f"fold_{k}" for k in range(1, 6)]
   importance_matrix = pd.DataFrame(
       np.clip(latent[:, None] + rng.normal(0, 0.03, size=(len(features), 5)), 0, None),
       index=features, columns=folds,
   )
   ax = feature_clustermap_static(
       importance_matrix,
       title="Feature clustering by importance signature (5 folds)",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_more/feature_clustermap_static.png" alt="feature_clustermap_static example output"><figcaption>Example output</figcaption></figure></div>
