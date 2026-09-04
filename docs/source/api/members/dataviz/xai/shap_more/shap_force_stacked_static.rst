dataviz.xai.shap_more.shap_force_stacked_static
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_force_stacked_static

Use case
--------

Use to visualize how each feature's contributions stack up across many instances relative to the base value.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_more import shap_force_stacked_static

   rng = np.random.default_rng(42)
   feature_names = [
       "tenure_months", "monthly_charges", "contract_two_year",
       "num_support_calls", "avg_session_min", "late_payments",
       "plan_premium", "age",
   ]
   scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3, 0.15, 0.1])
   shap_values = rng.normal(0, 1, size=(40, 8)) * scale
   ax = shap_force_stacked_static(
       shap_values, -1.10, feature_names, top_n=6,
       title="Stacked SHAP forces across 40 scored customers",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_force_stacked_static.png" alt="shap_force_stacked_static example output"><figcaption>Example output</figcaption></figure></div>
