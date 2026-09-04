dataviz.regression.prediction.prediction_plot_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction</p></div>

.. currentmodule:: dataviz.regression.prediction

.. autofunction:: prediction_plot_interactive

Use case
--------

Use to compare predicted against actual values with a perfect-prediction reference line for a quick fit-quality check.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.prediction import prediction_plot_interactive

   rng = np.random.default_rng(42)
   days = pd.date_range("2025-01-05", periods=24, freq="W")
   actual_demand = pd.Series(
       420 + 3.5 * np.arange(24) + rng.normal(0, 25, 24),
       index=days, name="actual_mwh",
   )
   predicted_demand = pd.Series(
       actual_demand + rng.normal(0, 18, 24), index=days, name="forecast_mwh"
   )

   fig = prediction_plot_interactive(
       actual_demand, predicted_demand,
       title="Weekly energy demand: forecast vs actual",
       marker_color="#2a6f97", marker_size=9,
       line_color="#d62728", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction/prediction_plot_interactive.png" alt="prediction_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
