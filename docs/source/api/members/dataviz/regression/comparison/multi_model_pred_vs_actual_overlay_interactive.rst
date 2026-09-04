dataviz.regression.comparison.multi_model_pred_vs_actual_overlay_interactive
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: multi_model_pred_vs_actual_overlay_interactive

Use case
--------

Use to overlay predicted-vs-actual scatters from several models and spot which one tracks the diagonal most tightly.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.comparison import multi_model_pred_vs_actual_overlay_interactive

   rng = np.random.default_rng(42)
   actual = pd.Series(rng.uniform(40, 160, 30), name="actual_throughput")
   preds = [actual + rng.normal(0, 6, 30),
            actual * rng.normal(1.0, 0.09, 30),
            actual + rng.normal(4, 10, 30)]
   labels = ["Linear", "Random Forest", "Gradient Boosting"]

   fig = multi_model_pred_vs_actual_overlay_interactive(
       actual, preds, labels,
       title="Line Throughput: Predicted vs Actual by Model",
       template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/multi_model_pred_vs_actual_overlay_interactive.png" alt="multi_model_pred_vs_actual_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
