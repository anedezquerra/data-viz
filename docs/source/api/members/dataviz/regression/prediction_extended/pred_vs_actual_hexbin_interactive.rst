dataviz.regression.prediction_extended.pred_vs_actual_hexbin_interactive
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction_extended</p></div>

.. currentmodule:: dataviz.regression.prediction_extended

.. autofunction:: pred_vs_actual_hexbin_interactive

Use case
--------

Use when many points overplot a predicted-vs-actual scatter; the 2-D histogram reveals where predictions concentrate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.prediction_extended import pred_vs_actual_hexbin_interactive

   rng = np.random.default_rng(42)
   batches = pd.Series(np.arange(1, 121), name="batch")
   actual_yield = pd.Series(
       rng.gamma(shape=9.0, scale=4.0, size=120), name="actual_yield_kg"
   )
   predicted_yield = pd.Series(
       0.85 * actual_yield + 5.0 + rng.normal(0, 3.5, 120), name="predicted_yield_kg"
   )

   fig = pred_vs_actual_hexbin_interactive(
       actual_yield, predicted_yield, nbins=18,
       title="Chemical batch yield: predicted vs actual density",
       colorscale="Cividis", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction_extended/pred_vs_actual_hexbin_interactive.png" alt="pred_vs_actual_hexbin_interactive example output"><figcaption>Example output</figcaption></figure></div>
