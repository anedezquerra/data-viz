dataviz.regression.prediction_extended.prediction_error_histogram_interactive
=============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.prediction_extended</p></div>

.. currentmodule:: dataviz.regression.prediction_extended

.. autofunction:: prediction_error_histogram_interactive

Use case
--------

Use to inspect the distribution of prediction errors for bias, skew, or heavy tails, optionally cumulatively.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.prediction_extended import prediction_error_histogram_interactive

   rng = np.random.default_rng(42)
   months = pd.date_range("2023-01-01", periods=30, freq="MS")
   actual_sales = pd.Series(
       980 + 12 * np.sin(np.arange(30) / 4.8) + rng.normal(0, 40, 30),
       index=months, name="actual_units",
   )
   forecast_sales = pd.Series(
       actual_sales + rng.normal(6, 28, 30), index=months, name="forecast_units"
   )

   fig = prediction_error_histogram_interactive(
       actual_sales, forecast_sales, bins=14,
       title="Retail sales forecast error distribution",
       color="#4878d0", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/prediction_extended/prediction_error_histogram_interactive.png" alt="prediction_error_histogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
