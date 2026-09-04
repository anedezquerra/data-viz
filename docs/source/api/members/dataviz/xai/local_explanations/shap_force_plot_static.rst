dataviz.xai.local_explanations.shap_force_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_explanations</p></div>

.. currentmodule:: dataviz.xai.local_explanations

.. autofunction:: shap_force_plot_static

Use case
--------

Use to explain one prediction as a horizontal push-pull of features from the base value to f(x), ideal for single-case narratives.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.local_explanations import shap_force_plot_static

   feature_names = [
       "tenure_months", "monthly_charges", "contract_two_year",
       "num_support_calls", "avg_session_min", "late_payments",
       "plan_premium", "age",
   ]
   shap_values_instance = np.array(
       [0.85, 0.42, -0.61, 0.37, 0.12, 0.28, -0.15, -0.06]
   )
   ax = shap_force_plot_static(
       shap_values_instance, feature_names, base_value=-1.10, top_n=8,
       title="Why customer #417 is predicted to churn (log-odds)",
   )
   ax.set_xlabel("Model output (log-odds of churn)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_explanations/shap_force_plot_static.png" alt="shap_force_plot_static example output"><figcaption>Example output</figcaption></figure></div>
