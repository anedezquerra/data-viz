dataviz.xai.shap_more.shap_temporal_drift_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_temporal_drift_static

Use case
--------

Use to track mean absolute SHAP per feature over time windows, detecting when the model's driving features drift.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.shap_more import shap_temporal_drift_static

   rng = np.random.default_rng(42)
   feature_names = [
       "tenure_months", "monthly_charges", "contract_two_year",
       "num_support_calls", "avg_session_min", "late_payments",
   ]
   n_days = 84
   timestamps = pd.Series(pd.date_range("2024-01-01", periods=n_days, freq="D"))
   scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3])
   shap_values = rng.normal(0, 1, size=(n_days, len(feature_names))) * scale
   trend = np.linspace(0, 0.5, n_days)
   shap_values[:, 3] = shap_values[:, 3] + trend
   ax = shap_temporal_drift_static(
       timestamps, shap_values, feature_names, freq="W", top_n=4,
       title="Weekly SHAP drift - support calls gain importance",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_temporal_drift_static.png" alt="shap_temporal_drift_static example output"><figcaption>Example output</figcaption></figure></div>
