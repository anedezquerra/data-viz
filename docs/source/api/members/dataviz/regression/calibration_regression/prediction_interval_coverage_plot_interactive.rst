dataviz.regression.calibration_regression.prediction_interval_coverage_plot_interactive
=======================================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.calibration_regression</p></div>

.. currentmodule:: dataviz.regression.calibration_regression

.. autofunction:: prediction_interval_coverage_plot_interactive

Use case
--------

Use to verify that nominal prediction intervals (e.g. 90%) actually cover the observed target at the advertised rate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.calibration_regression import prediction_interval_coverage_plot_interactive

   rng = np.random.default_rng(42)
   n = 40
   forecast = pd.Series(rng.uniform(50, 150, n), name="forecast_demand")
   observed = pd.Series(forecast + rng.normal(0, 12, n), name="observed_demand")

   fig = prediction_interval_coverage_plot_interactive(
       observed, forecast,
       levels=(0.5, 0.7, 0.8, 0.9, 0.95), method="empirical",
       title="Spare-Parts Demand: Interval Coverage",
       coverage_color="#2a7f62", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/calibration_regression/prediction_interval_coverage_plot_interactive.png" alt="prediction_interval_coverage_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
