dataviz.regression.forecast.forecast_vs_actual_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: forecast_vs_actual_interactive

Use case
--------

Use to overlay actual and forecast series and spot systematic over- or under-prediction over time.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import forecast_vs_actual_interactive

   rng = np.random.default_rng(42)
   weeks = pd.date_range("2025-01-06", periods=24, freq="W-MON")
   seasonal = 4.0 * np.sin(2 * np.pi * np.arange(24) / 12.0)
   actual = pd.Series(52.0 + seasonal + rng.normal(0, 1.5, 24), index=weeks,
                      name="weekly_demand_kwh")
   forecast = pd.Series(52.0 + seasonal + rng.normal(0, 0.9, 24), index=weeks,
                        name="arima_forecast")

   fig = forecast_vs_actual_interactive(weeks, actual, forecast,
                                        title="Plant Energy Demand: ARIMA Forecast vs Actual",
                                        template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/forecast_vs_actual_interactive.png" alt="forecast_vs_actual_interactive example output"><figcaption>Example output</figcaption></figure></div>
