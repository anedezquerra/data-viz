dataviz.xai.importance_extra.feature_importance_grouped_bar_static
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: feature_importance_grouped_bar_static

Use case
--------

Compare importance rankings across multiple models to confirm key drivers are consistent before deployment.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.importance_extra import feature_importance_grouped_bar_static

   features = [
       "credit_score", "debt_to_income", "utilization",
       "annual_income", "loan_amount", "account_age",
   ]
   importances = {
       "LogisticReg": dict(zip(features, [0.35, 0.22, 0.15, 0.12, 0.09, 0.07])),
       "RandomForest": dict(zip(features, [0.28, 0.25, 0.18, 0.11, 0.10, 0.08])),
       "XGBoost": dict(zip(features, [0.31, 0.21, 0.20, 0.10, 0.12, 0.06])),
   }

   ax = feature_importance_grouped_bar_static(
       importances,
       top_n=6,
       title="Feature Importance Agreement Across Candidate Models",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_extra/feature_importance_grouped_bar_static.png" alt="feature_importance_grouped_bar_static example output"><figcaption>Example output</figcaption></figure></div>
