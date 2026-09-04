dataviz.xai.importance_more.importance_stability_plot_interactive
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: importance_stability_plot_interactive

Use case
--------

Use to check whether feature rankings are stable across CV folds or seeds; wide error bars flag unreliable importances.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.xai.importance_more import importance_stability_plot_interactive

   rng = np.random.default_rng(42)
   features = [
       "credit_score", "debt_to_income", "loan_amount",
       "employment_years", "annual_income", "num_open_accounts",
   ]
   base = np.array([0.42, 0.31, 0.24, 0.18, 0.15, 0.09])
   folds = np.clip(base + rng.normal(0, 0.03, size=(8, len(features))), 0, None)
   fold_importances = pd.DataFrame(
       folds, columns=features,
       index=[f"fold_{k}" for k in range(1, 9)],
   )
   fig = importance_stability_plot_interactive(
       fold_importances, top_n=6,
       title="Permutation importance stability across 8 CV folds",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_more/importance_stability_plot_interactive.png" alt="importance_stability_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
