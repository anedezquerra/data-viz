dataviz.xai.local_explanations.shap_decision_plot_interactive
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_explanations</p></div>

.. currentmodule:: dataviz.xai.local_explanations

.. autofunction:: shap_decision_plot_interactive

Use case
--------

Use to trace cumulative SHAP paths from base to prediction for many instances at once, exposing typical and atypical decision routes.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.local_explanations import shap_decision_plot_interactive

   rng = np.random.default_rng(42)
   feature_names = [
       "tenure_months", "monthly_charges", "contract_two_year",
       "num_support_calls", "avg_session_min", "late_payments",
       "plan_premium", "age",
   ]
   scale = np.array([0.8, 0.4, 0.6, 0.35, 0.15, 0.3, 0.15, 0.1])
   shap_values = rng.normal(0, 1, size=(25, 8)) * scale
   fig = shap_decision_plot_interactive(
       shap_values, feature_names, base_value=-1.10, top_n=8,
       title="Decision paths for 25 churn-model customers",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_explanations/shap_decision_plot_interactive.png" alt="shap_decision_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
