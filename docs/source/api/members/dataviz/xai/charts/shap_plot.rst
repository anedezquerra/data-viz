dataviz.xai.charts.shap_plot
============================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.charts</p></div>

.. currentmodule:: dataviz.xai.charts

.. autofunction:: shap_plot

Use case
--------

Use to explain individual and global predictions with SHAP values during model review or debugging.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.charts import shap_plot

   rng = np.random.default_rng(42)
   features = [
       "tenure_months", "monthly_charges", "support_tickets", "contract_type",
       "num_products", "payment_delay", "usage_score", "discount_pct",
   ]
   scales = np.array([0.45, 0.30, 0.22, 0.15, 0.10, 0.07, 0.05, 0.03])
   shap_values = rng.normal(0.0, scales, size=(80, len(features)))

   ax = shap_plot(
       shap_values,
       features,
       title="SHAP Feature Impact: Subscription Churn Model",
       color="teal",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/charts/shap_plot.png" alt="shap_plot example output"><figcaption>Example output</figcaption></figure></div>
