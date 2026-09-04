dataviz.xai.importance_more.feature_clustermap_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: feature_clustermap_interactive

Use case
--------

Use to group features that share an importance signature across models or folds, revealing redundant or cohort-specific signals.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.xai.importance_more import feature_clustermap_interactive

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "loan_amount", "annual_income",
       "employment_years", "num_open_accounts", "age", "num_credit_cards",
   ]
   latent = np.array([0.40, 0.38, 0.25, 0.23, 0.18, 0.10, 0.09, 0.07])
   folds = [f"fold_{k}" for k in range(1, 6)]
   importance_matrix = pd.DataFrame(
       np.clip(latent[:, None] + rng.normal(0, 0.03, size=(len(features), 5)), 0, None),
       index=features, columns=folds,
   )
   fig = feature_clustermap_interactive(
       importance_matrix,
       title="Feature clustering by importance signature (5 folds)",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_more/feature_clustermap_interactive.png" alt="feature_clustermap_interactive example output"><figcaption>Example output</figcaption></figure></div>
