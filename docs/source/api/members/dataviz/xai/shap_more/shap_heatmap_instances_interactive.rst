dataviz.xai.shap_more.shap_heatmap_instances_interactive
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_heatmap_instances_interactive

Use case
--------

Use to spot clusters of similarly explained instances by plotting the SHAP matrix sorted by instance similarity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.shap_more import shap_heatmap_instances_interactive

   rng = np.random.default_rng(42)
   feature_names = [
       "credit_score", "debt_to_income", "loan_amount",
       "employment_years", "annual_income", "late_payments",
       "num_open_accounts", "age",
   ]
   coef = np.array([-0.6, 0.5, 0.3, -0.25, -0.2, 0.35, 0.1, -0.05])
   group_a = rng.normal(-1, 0.5, size=(20, 8)) * coef
   group_b = rng.normal(1, 0.5, size=(20, 8)) * coef
   shap_values = np.vstack([group_a, group_b])
   fig = shap_heatmap_instances_interactive(
       shap_values, feature_names, top_n_features=8,
       title="Per-instance SHAP heatmap reveals two applicant segments",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_heatmap_instances_interactive.png" alt="shap_heatmap_instances_interactive example output"><figcaption>Example output</figcaption></figure></div>
