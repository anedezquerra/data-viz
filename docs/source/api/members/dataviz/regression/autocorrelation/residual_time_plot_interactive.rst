dataviz.regression.autocorrelation.residual_time_plot_interactive
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.autocorrelation</p></div>

.. currentmodule:: dataviz.regression.autocorrelation

.. autofunction:: residual_time_plot_interactive

Use case
--------

Use to plot residuals over time or observation order to reveal drift, trends, or regime changes hidden by aggregate metrics.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.autocorrelation import residual_time_plot_interactive

   rng = np.random.default_rng(42)
   days = pd.date_range("2024-01-01", periods=30, freq="D")
   load = pd.Series(85 + 6 * np.sin(np.arange(30) / 4.5) + rng.normal(0, 2.0, 30),
                    name="plant_load_mw")
   fitted = pd.Series(85 + 6 * np.sin(np.arange(30) / 4.5), name="forecast_mw")

   fig = residual_time_plot_interactive(load, fitted, time=days,
                                        title="Energy Load Forecast: Residuals Over Time",
                                        color="#b25b16", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/autocorrelation/residual_time_plot_interactive.png" alt="residual_time_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
