dataviz.xai.comparison.shap_model_agreement_scatter_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.comparison</p></div>

.. currentmodule:: dataviz.xai.comparison

.. autofunction:: shap_model_agreement_scatter_interactive

Use case
--------

Check whether two models attribute predictions to the same features per instance, quantified by Pearson r.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.comparison import shap_model_agreement_scatter_interactive

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "utilization",
       "annual_income", "loan_amount", "account_age",
   ]
   base = rng.normal(0.0, [0.40, 0.30, 0.25, 0.15, 0.10, 0.05], size=(60, 6))
   shap_rf = base + rng.normal(0.0, 0.05, size=base.shape)
   shap_xgb = base * 1.1 + rng.normal(0.0, 0.08, size=base.shape)

   fig = shap_model_agreement_scatter_interactive(
       shap_rf,
       shap_xgb,
       model_a="RandomForest",
       model_b="XGBoost",
       feature_names=features,
       title="Per-Instance SHAP Agreement: RandomForest vs XGBoost",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/comparison/shap_model_agreement_scatter_interactive.png" alt="shap_model_agreement_scatter_interactive example output"><figcaption>Example output</figcaption></figure></div>
