dataviz.xai.shap_more.shap_main_vs_interaction_bar_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_more</p></div>

.. currentmodule:: dataviz.xai.shap_more

.. autofunction:: shap_main_vs_interaction_bar_interactive

Use case
--------

Use to decompose each feature's impact into main effects versus interaction effects, flagging features that only matter in combination.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.shap_more import shap_main_vs_interaction_bar_interactive

   rng = np.random.default_rng(42)
   feature_names = [
       "tenure_months", "monthly_charges", "contract_two_year",
       "num_support_calls", "avg_session_min", "late_payments",
       "plan_premium", "age",
   ]
   main_scale = np.array([0.7, 0.45, 0.5, 0.3, 0.15, 0.28, 0.12, 0.08])
   inter_scale = np.array([0.15, 0.25, 0.08, 0.12, 0.05, 0.07, 0.04, 0.02])
   main_effects = rng.normal(0, 1, size=(60, 8)) * main_scale
   interaction_effects = rng.normal(0, 1, size=(60, 8)) * inter_scale
   fig = shap_main_vs_interaction_bar_interactive(
       main_effects, interaction_effects, feature_names, top_n=8,
       title="Main effects dominate, but charges interact strongly",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/shap_more/shap_main_vs_interaction_bar_interactive.png" alt="shap_main_vs_interaction_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
