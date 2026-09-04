dataviz.xai.comparison.rashomon_importance_band_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.comparison</p></div>

.. currentmodule:: dataviz.xai.comparison

.. autofunction:: rashomon_importance_band_static

Use case
--------

Use when several near-optimal models disagree, to show the min-to-max range of plausible feature importances.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.comparison import rashomon_importance_band_static

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "utilization", "annual_income",
       "loan_amount", "account_age", "inquiries_6m", "open_accounts",
   ]
   medians = np.array([0.30, 0.22, 0.16, 0.11, 0.08, 0.06, 0.04, 0.03])
   models = [f"Rashomon-{i:02d}" for i in range(1, 9)]
   importances = pd.DataFrame(
       medians[:, None] + rng.normal(0, 0.025, size=(len(features), len(models))),
       index=features,
       columns=models,
   )

   ax = rashomon_importance_band_static(
       importances,
       top_n=8,
       title="Importance Stability Across the Rashomon Set (8 Near-Optimal Models)",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/comparison/rashomon_importance_band_static.png" alt="rashomon_importance_band_static example output"><figcaption>Example output</figcaption></figure></div>
