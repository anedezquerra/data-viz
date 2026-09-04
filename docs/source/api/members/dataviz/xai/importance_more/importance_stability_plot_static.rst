dataviz.xai.importance_more.importance_stability_plot_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: importance_stability_plot_static

Use case
--------

Use to check whether feature rankings are stable across CV folds or seeds; wide error bars flag unreliable importances.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.importance_more import importance_stability_plot_static

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "loan_amount",
       "employment_years", "annual_income", "num_open_accounts",
   ]
   base = np.array([0.42, 0.31, 0.24, 0.18, 0.15, 0.09])
   folds = np.clip(base + rng.normal(0, 0.03, size=(8, len(features))), 0, None)
   fold_importances = pd.DataFrame(
       folds, columns=features,
       index=[f"fold_{k}" for k in range(1, 9)],
   )
   ax = importance_stability_plot_static(
       fold_importances, top_n=6,
       title="Permutation importance stability across 8 CV folds",
   )
   ax.set_xlabel("Mean decrease in ROC AUC")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_more/importance_stability_plot_static.png" alt="importance_stability_plot_static example output"><figcaption>Example output</figcaption></figure></div>
