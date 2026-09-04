dataviz.regression.autocorrelation.residual_pacf_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.autocorrelation</p></div>

.. currentmodule:: dataviz.regression.autocorrelation

.. autofunction:: residual_pacf_interactive

Use case
--------

Use to identify the direct lag order of residual dependence when choosing an AR term or diagnosing model misspecification.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.autocorrelation import residual_pacf_interactive

   rng = np.random.default_rng(42)
   week = np.arange(30)
   sales = pd.Series(1200 + 40 * np.sin(week / 2.5) + rng.normal(0, 25, 30),
                     name="weekly_units")
   fitted = pd.Series(1200 + 38 * np.sin(week / 2.5), name="fitted_units")

   fig = residual_pacf_interactive(sales, fitted, max_lag=10,
                                   title="Weekly Demand Model: Residual PACF",
                                   color="#8c5aa8", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/autocorrelation/residual_pacf_interactive.png" alt="residual_pacf_interactive example output"><figcaption>Example output</figcaption></figure></div>
