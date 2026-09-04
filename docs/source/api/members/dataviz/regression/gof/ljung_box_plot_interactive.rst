dataviz.regression.gof.ljung_box_plot_interactive
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.gof</p></div>

.. currentmodule:: dataviz.regression.gof

.. autofunction:: ljung_box_plot_interactive

Use case
--------

Use to plot Ljung-Box p-values across lags to detect residual autocorrelation after fitting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.gof import ljung_box_plot_interactive

   rng = np.random.default_rng(42)
   n = 30
   noise = rng.normal(0.0, 1.0, n)
   residuals = pd.Series(
       np.array([noise[0]] + [0.6 * noise[i - 1] + noise[i] for i in range(1, n)]),
       index=pd.date_range("2025-04-01", periods=n, freq="D"),
       name="daily_yield_residuals")

   fig = ljung_box_plot_interactive(residuals, lags=12, alpha=0.05,
                                    title="Crop Yield Model: Ljung-Box p-values",
                                    template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/gof/ljung_box_plot_interactive.png" alt="ljung_box_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
