dataviz.xai.dependence_more.h_statistic_heatmap_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: h_statistic_heatmap_interactive

Use case
--------

Use to screen for pairwise feature interactions with Friedman's H-statistic before deeper interaction analysis.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.dependence_more import h_statistic_heatmap_interactive

   features = [
       "credit_score", "debt_to_income", "utilization", "annual_income", "loan_amount",
   ]
   h = np.array([
       [1.00, 0.34, 0.41, 0.05, 0.08],
       [0.34, 1.00, 0.52, 0.07, 0.12],
       [0.41, 0.52, 1.00, 0.04, 0.15],
       [0.05, 0.07, 0.04, 1.00, 0.22],
       [0.08, 0.12, 0.15, 0.22, 1.00],
   ])
   h_matrix = pd.DataFrame(h, index=features, columns=features)

   fig = h_statistic_heatmap_interactive(
       h_matrix,
       title="Friedman H-Statistic - Default Model Feature Interactions",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/dependence_more/h_statistic_heatmap_interactive.png" alt="h_statistic_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
