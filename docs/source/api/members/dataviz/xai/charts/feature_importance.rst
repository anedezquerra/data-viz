dataviz.xai.charts.feature_importance
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.charts</p></div>

.. currentmodule:: dataviz.xai.charts

.. autofunction:: feature_importance

Use case
--------

Use when presenting which features drive a model's predictions to non-technical stakeholders.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.charts import feature_importance

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "payment_history", "utilization",
       "annual_income", "loan_amount", "account_age", "inquiries_6m",
   ]
   weights = np.array([0.31, 0.22, 0.17, 0.11, 0.08, 0.05, 0.04, 0.02])
   importances = pd.Series(
       weights + rng.normal(0, 0.004, size=len(features)), index=features
   )

   ax = feature_importance(
       importances,
       title="Credit-Risk Model: Gradient-Boosting Feature Importance",
       top_n=8,
   )
   ax.set_xlabel("Mean decrease in impurity")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/charts/feature_importance.png" alt="feature_importance example output"><figcaption>Example output</figcaption></figure></div>
