dataviz.xai.dependence_more.interaction_network_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: interaction_network_interactive

Use case
--------

Use to communicate the strongest feature interactions as a network graph for reports or presentations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.dependence_more import interaction_network_interactive

   features = [
       "credit_score", "debt_to_income", "utilization",
       "annual_income", "loan_amount", "account_age",
   ]
   h = np.array([
       [0.00, 0.34, 0.41, 0.05, 0.08, 0.03],
       [0.34, 0.00, 0.52, 0.07, 0.12, 0.04],
       [0.41, 0.52, 0.00, 0.04, 0.15, 0.06],
       [0.05, 0.07, 0.04, 0.00, 0.22, 0.18],
       [0.08, 0.12, 0.15, 0.22, 0.00, 0.05],
       [0.03, 0.04, 0.06, 0.18, 0.05, 0.00],
   ])
   interaction_matrix = pd.DataFrame(h, index=features, columns=features)

   fig = interaction_network_interactive(
       interaction_matrix,
       threshold=0.12,
       title="Strongest Feature Interactions - Default Risk Model",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/dependence_more/interaction_network_interactive.png" alt="interaction_network_interactive example output"><figcaption>Example output</figcaption></figure></div>
