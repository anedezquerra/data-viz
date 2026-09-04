dataviz.xai.feature_imp.feature_importance_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.feature_imp</p></div>

.. currentmodule:: dataviz.xai.feature_imp

.. autofunction:: feature_importance_interactive

Use case
--------

Use when presenting which features drive a model's predictions to non-technical stakeholders.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.feature_imp import feature_importance_interactive

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "payment_history", "utilization",
       "annual_income", "loan_amount", "account_age", "inquiries_6m",
       "open_accounts", "delinquencies",
   ]
   weights = np.array([0.28, 0.20, 0.16, 0.12, 0.08, 0.06, 0.04, 0.03, 0.02, 0.01])
   importances = pd.Series(
       weights + rng.normal(0, 0.003, size=len(features)), index=features
   )

   fig = feature_importance_interactive(
       importances,
       title="Credit-Risk Model: Top Feature Importances",
       top_n=8,
       xlabel="Mean decrease in impurity",
       marker_color="darkslateblue",
       height=560,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/feature_imp/feature_importance_interactive.png" alt="feature_importance_interactive example output"><figcaption>Example output</figcaption></figure></div>
