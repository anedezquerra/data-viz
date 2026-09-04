dataviz.xai.shap_extra.shap_interaction_heatmap_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_interaction_heatmap_interactive

Use case
--------

Use to find which feature pairs carry the strongest SHAP interaction effects before drilling into dependence plots.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.shap_extra import shap_interaction_heatmap_interactive

   feature_names = [
       "tenure_months", "monthly_charges", "contract_two_year",
       "num_support_calls", "avg_session_min", "late_payments",
       "plan_premium", "age",
   ]
   diag = np.array([0.55, 0.40, 0.38, 0.30, 0.16, 0.26, 0.12, 0.09])
   off = np.array([
       [0.00, 0.21, 0.12, 0.10, 0.05, 0.06, 0.03, 0.02],
       [0.21, 0.00, 0.09, 0.08, 0.04, 0.05, 0.04, 0.02],
       [0.12, 0.09, 0.00, 0.06, 0.03, 0.04, 0.05, 0.01],
       [0.10, 0.08, 0.06, 0.00, 0.04, 0.07, 0.02, 0.02],
       [0.05, 0.04, 0.03, 0.04, 0.00, 0.02, 0.02, 0.01],
       [0.06, 0.05, 0.04, 0.07, 0.02, 0.00, 0.01, 0.01],
       [0.03, 0.04, 0.05, 0.02, 0.02, 0.01, 0.00, 0.01],
       [0.02, 0.02, 0.01, 0.02, 0.01, 0.01, 0.01, 0.00],
   ])
   interaction_matrix = off + np.diag(diag)
   fig = shap_interaction_heatmap_interactive(
       interaction_matrix, feature_names, top_n=8,
       title="Mean absolute SHAP interactions - churn model",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_extra/shap_interaction_heatmap_interactive.png" alt="shap_interaction_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
