dataviz.regression.prediction_extended.pred_vs_actual_density_interactive
=========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction_extended</p></div>

.. currentmodule:: dataviz.regression.prediction_extended

.. autofunction:: pred_vs_actual_density_interactive

Use case
--------

Use to compare the marginal distributions of actual and predicted values and expose systematic shift or shrinkage.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.prediction_extended import pred_vs_actual_density_interactive

   rng = np.random.default_rng(42)
   rides = pd.Series(np.arange(1, 61), name="ride")
   actual_fare = pd.Series(rng.lognormal(2.8, 0.45, 60), name="actual_fare_usd")
   predicted_fare = pd.Series(
       0.9 * actual_fare + 1.5 + rng.normal(0, 1.8, 60), name="predicted_fare_usd"
   )

   fig = pred_vs_actual_density_interactive(
       actual_fare, predicted_fare, bins=24,
       title="Ride-hailing fares: actual vs predicted distributions",
       actual_color="#4878d0", predicted_color="#ee854a",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction_extended/pred_vs_actual_density_interactive.png" alt="pred_vs_actual_density_interactive example output"><figcaption>Example output</figcaption></figure></div>
