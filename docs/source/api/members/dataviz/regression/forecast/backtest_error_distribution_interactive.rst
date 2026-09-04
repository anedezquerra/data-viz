dataviz.regression.forecast.backtest_error_distribution_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: backtest_error_distribution_interactive

Use case
--------

Use to inspect the distribution of backtest errors for bias, skew, and heavy tails.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import backtest_error_distribution_interactive

   rng = np.random.default_rng(42)
   backtest_errors = pd.Series(
       rng.normal(0.5, 4.0, 400) + rng.choice([0.0, 6.0], size=400, p=[0.9, 0.1]),
       name="backtest_error_bbl")

   fig = backtest_error_distribution_interactive(
       backtest_errors,
       title="Oil Production Forecast: Backtest Error Distribution",
       nbins=40, color="#17becf", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/backtest_error_distribution_interactive.png" alt="backtest_error_distribution_interactive example output"><figcaption>Example output</figcaption></figure></div>
