dataviz.xai.local_explanations.shap_decision_plot_static
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_explanations</p></div>

.. currentmodule:: dataviz.xai.local_explanations

.. autofunction:: shap_decision_plot_static

Use case
--------

Use to trace cumulative SHAP paths from base to prediction for many instances at once, exposing typical and atypical decision routes.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.local_explanations import shap_decision_plot_static

   rng = np.random.default_rng(42)
   feature_names = [
       "tenure_months", "monthly_charges", "contract_two_year",
       "num_support_calls", "avg_session_min", "late_payments",
       "plan_premium", "age",
   ]
   scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3, 0.15, 0.1])
   shap_values = rng.normal(0, 1, size=(25, 8)) * scale
   ax = shap_decision_plot_static(
       shap_values, feature_names, base_value=-1.10, top_n=8,
       title="Decision paths for 25 churn-model customers",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_explanations/shap_decision_plot_static.png" alt="shap_decision_plot_static example output"><figcaption>Example output</figcaption></figure></div>
