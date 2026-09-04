dataviz.xai.importance_more.importance_correlation_heatmap_interactive
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: importance_correlation_heatmap_interactive

Use case
--------

Use to verify that different models agree on which features matter by correlating their importance vectors.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.xai.importance_more import importance_correlation_heatmap_interactive

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "loan_amount",
       "employment_years", "annual_income", "num_open_accounts", "age",
   ]
   latent = np.array([0.40, 0.30, 0.24, 0.18, 0.15, 0.10, 0.08])
   models = ["xgboost", "lightgbm", "random_forest", "logistic"]
   data = {
       m: np.clip(latent + rng.normal(0, 0.04, size=len(features)), 0, None)
       for m in models
   }
   importances_by_model = pd.DataFrame(data, index=features)
   fig = importance_correlation_heatmap_interactive(
       importances_by_model,
       title="Do four churn models agree on feature importance?",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_more/importance_correlation_heatmap_interactive.png" alt="importance_correlation_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
