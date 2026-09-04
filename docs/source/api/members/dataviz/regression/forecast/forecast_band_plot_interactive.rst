dataviz.regression.forecast.forecast_band_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: forecast_band_plot_interactive

Use case
--------

Use to show the forecast path with its prediction band and check how often actuals fall inside it.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import forecast_band_plot_interactive

   rng = np.random.default_rng(42)
   days = pd.date_range("2025-03-01", periods=20, freq="D")
   trend = 120.0 + 0.8 * np.arange(20)
   central = pd.Series(trend + rng.normal(0, 1.0, 20), index=days,
                       name="price_forecast")
   actual = pd.Series(trend + rng.normal(0, 3.0, 20), index=days,
                      name="spot_price")
   lower = central - 5.0
   upper = central + 5.0

   fig = forecast_band_plot_interactive(
       days, actual, central, lower, upper,
       title="Wholesale Coffee Price: Forecast with 90% Band",
       template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/forecast_band_plot_interactive.png" alt="forecast_band_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
