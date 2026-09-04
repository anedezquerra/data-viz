dataviz.regression.forecast.rolling_forecast_origin_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: rolling_forecast_origin_interactive

Use case
--------

Use to check forecast stability by plotting scores across rolling forecast origins.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import rolling_forecast_origin_interactive

   rng = np.random.default_rng(42)
   origins = pd.date_range("2024-01-31", periods=18, freq="ME")
   mape_scores = pd.Series(8.5 - 0.15 * np.arange(18) + rng.normal(0, 0.6, 18),
                           index=origins, name="mape_pct")

   fig = rolling_forecast_origin_interactive(
       origins, mape_scores,
       title="Retail Sales Model: MAPE Across Rolling Origins",
       color="#9467bd", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/rolling_forecast_origin_interactive.png" alt="rolling_forecast_origin_interactive example output"><figcaption>Example output</figcaption></figure></div>
