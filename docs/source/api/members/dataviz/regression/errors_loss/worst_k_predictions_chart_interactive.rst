dataviz.regression.errors_loss.worst_k_predictions_chart_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.errors_loss</p></div>

.. currentmodule:: dataviz.regression.errors_loss

.. autofunction:: worst_k_predictions_chart_interactive

Use case
--------

Use to surface the k predictions with the largest absolute error for targeted inspection and debugging.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.errors_loss import worst_k_predictions_chart_interactive

   rng = np.random.default_rng(42)
   actual = pd.Series(rng.uniform(10, 120, 25), name="actual_los_days")
   predicted = pd.Series(actual + rng.normal(0, 9, 25), name="predicted_los_days")

   fig = worst_k_predictions_chart_interactive(
       actual, predicted, k=8,
       title="Hospital Stay Model: 8 Worst Predictions",
       color="#c0392b", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/errors_loss/worst_k_predictions_chart_interactive.png" alt="worst_k_predictions_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
