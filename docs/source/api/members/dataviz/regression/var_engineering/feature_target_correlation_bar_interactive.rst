dataviz.regression.var_engineering.feature_target_correlation_bar_interactive
=============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.var_engineering</p></div>

.. currentmodule:: dataviz.regression.var_engineering

.. autofunction:: feature_target_correlation_bar_interactive

Use case
--------

Use to rank features by Pearson correlation with the target, sorted by magnitude, as a quick univariate screen before modeling.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.var_engineering import feature_target_correlation_bar_interactive

   rng = np.random.default_rng(42)
   n = 50
   temp = rng.uniform(15, 35, n)
   humidity = rng.uniform(20, 95, n)
   wind = rng.uniform(0, 40, n)
   pressure = rng.uniform(1005, 1025, n)
   rentals = 30 + 4.2 * temp - 0.9 * humidity + rng.normal(0, 12, n)
   X = pd.DataFrame({
       "temperature": temp, "humidity": humidity,
       "wind_speed": wind, "pressure": pressure,
   })

   fig = feature_target_correlation_bar_interactive(
       X, rentals, feature_names=list(X.columns),
       title="Bike-share demand: feature-target Pearson correlations",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/var_engineering/feature_target_correlation_bar_interactive.png" alt="feature_target_correlation_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
