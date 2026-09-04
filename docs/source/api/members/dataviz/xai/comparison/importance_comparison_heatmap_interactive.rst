dataviz.xai.comparison.importance_comparison_heatmap_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.comparison</p></div>

.. currentmodule:: dataviz.xai.comparison

.. autofunction:: importance_comparison_heatmap_interactive

Use case
--------

Use to compare feature importances across several models side by side before selecting a champion model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.comparison import importance_comparison_heatmap_interactive

   features = [
       "credit_score", "debt_to_income", "utilization",
       "annual_income", "loan_amount", "account_age",
   ]
   importance_matrix = pd.DataFrame(
       {
           "LogisticReg": [0.35, 0.22, 0.15, 0.12, 0.09, 0.07],
           "RandomForest": [0.28, 0.25, 0.18, 0.11, 0.10, 0.08],
           "XGBoost": [0.31, 0.21, 0.20, 0.10, 0.12, 0.06],
           "MLP": [0.26, 0.19, 0.22, 0.14, 0.11, 0.08],
       },
       index=features,
   )

   fig = importance_comparison_heatmap_interactive(
       importance_matrix,
       title="Default-Model Importance Agreement Across Algorithms",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/comparison/importance_comparison_heatmap_interactive.png" alt="importance_comparison_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
