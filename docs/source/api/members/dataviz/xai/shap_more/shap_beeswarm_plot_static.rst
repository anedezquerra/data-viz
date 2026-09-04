dataviz.xai.shap_more.shap_beeswarm_plot_static
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_beeswarm_plot_static

Use case
--------

Use as a density-jittered SHAP beeswarm colored by feature value; tighter packing than the dot summary for large datasets.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_more import shap_beeswarm_plot_static

   rng = np.random.default_rng(42)
   feature_names = [
       "credit_score", "debt_to_income", "loan_amount",
       "employment_years", "annual_income", "late_payments",
       "num_open_accounts", "age",
   ]
   X = rng.normal(0, 1, size=(80, 8))
   coef = np.array([-0.6, 0.5, 0.3, -0.25, -0.2, 0.35, 0.1, -0.05])
   shap_values = X * coef + rng.normal(0, 0.05, size=(80, 8))
   ax = shap_beeswarm_plot_static(
       shap_values, X, feature_names, top_n=8,
       title="SHAP beeswarm - credit default model (80 applicants)",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_beeswarm_plot_static.png" alt="shap_beeswarm_plot_static example output"><figcaption>Example output</figcaption></figure></div>
