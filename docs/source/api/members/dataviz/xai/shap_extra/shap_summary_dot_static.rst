dataviz.xai.shap_extra.shap_summary_dot_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_summary_dot_static

Use case
--------

Use as the canonical SHAP beeswarm: per-instance SHAP values per feature, colored by feature value to expose direction and spread.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_extra import shap_summary_dot_static

   rng = np.random.default_rng(42)
   feature_names = [
       "tenure_months", "monthly_charges", "contract_two_year",
       "num_support_calls", "avg_session_min", "late_payments",
       "plan_premium", "age",
   ]
   X = rng.normal(0, 1, size=(60, 8))
   coef = np.array([-0.7, 0.4, -0.5, 0.35, -0.15, 0.3, 0.1, -0.08])
   shap_values = X * coef + rng.normal(0, 0.05, size=(60, 8))
   ax = shap_summary_dot_static(
       shap_values, X, feature_names, top_n=8,
       title="SHAP summary - telecom churn model (60 customers)",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_extra/shap_summary_dot_static.png" alt="shap_summary_dot_static example output"><figcaption>Example output</figcaption></figure></div>
