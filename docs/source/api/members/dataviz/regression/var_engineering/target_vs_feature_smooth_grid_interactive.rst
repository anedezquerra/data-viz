dataviz.regression.var_engineering.target_vs_feature_smooth_grid_interactive
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.var_engineering</p></div>

.. currentmodule:: dataviz.regression.var_engineering

.. autofunction:: target_vs_feature_smooth_grid_interactive

Use case
--------

Use in early EDA to screen many features at once via smoothed E[y|x] curves and spot which predictors have nonlinear target relationships.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.var_engineering import target_vs_feature_smooth_grid_interactive

   rng = np.random.default_rng(42)
   n = 60
   X = pd.DataFrame({
       "temperature": rng.uniform(15, 35, n),
       "humidity": rng.uniform(20, 95, n),
       "wind_speed": rng.uniform(0, 40, n),
       "hour": rng.uniform(0, 24, n),
   })
   rentals = (30 + 4.2 * X["temperature"] - 0.9 * X["humidity"]
              + 18 * np.sin(X["hour"] / 24 * 2 * np.pi)
              + rng.normal(0, 12, n))

   fig = target_vs_feature_smooth_grid_interactive(
       X, rentals, feature_names=list(X.columns), bins=15, ncols=2,
       title="Bike-share demand: smoothed target vs each feature",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/var_engineering/target_vs_feature_smooth_grid_interactive.png" alt="target_vs_feature_smooth_grid_interactive example output"><figcaption>Example output</figcaption></figure></div>
