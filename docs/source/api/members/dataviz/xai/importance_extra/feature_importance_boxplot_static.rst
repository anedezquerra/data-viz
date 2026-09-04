dataviz.xai.importance_extra.feature_importance_boxplot_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: feature_importance_boxplot_static

Use case
--------

Use to assess the stability of importance estimates across CV folds or repeated runs via per-feature spread.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.importance_extra import feature_importance_boxplot_static

   rng = np.random.default_rng(42)
   centers = {
       "credit_score": 0.142,
       "debt_to_income": 0.098,
       "utilization": 0.071,
       "payment_history": 0.055,
       "annual_income": 0.031,
       "loan_amount": 0.024,
       "account_age": 0.012,
   }
   per_fold = {
       name: list(rng.normal(c, 0.008, size=12)) for name, c in centers.items()
   }

   ax = feature_importance_boxplot_static(
       per_fold,
       top_n=7,
       title="Permutation Importance Stability Across 12 Repeats",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_extra/feature_importance_boxplot_static.png" alt="feature_importance_boxplot_static example output"><figcaption>Example output</figcaption></figure></div>
