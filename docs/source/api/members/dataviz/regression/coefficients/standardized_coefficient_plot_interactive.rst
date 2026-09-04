dataviz.regression.coefficients.standardized_coefficient_plot_interactive
=========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.coefficients</p></div>

.. currentmodule:: dataviz.regression.coefficients

.. autofunction:: standardized_coefficient_plot_interactive

Use case
--------

Use to compare relative feature importance on a common scale via beta times sigma_x over sigma_y, when raw units are not comparable.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.coefficients import standardized_coefficient_plot_interactive

   rng = np.random.default_rng(42)
   n = 30
   X = pd.DataFrame({
       "miles_driven_k": rng.uniform(2, 25, n),
       "vehicle_age_yr": rng.uniform(0, 15, n),
       "engine_l": rng.uniform(1.2, 5.0, n),
   })
   y = pd.Series(300 + 18 * X["miles_driven_k"] + 45 * X["vehicle_age_yr"]
                 + 30 * X["engine_l"] + rng.normal(0, 60, n),
                 name="annual_maintenance_usd")

   fig = standardized_coefficient_plot_interactive(
       X, y, feature_names=list(X.columns),
       title="Fleet Maintenance Cost: Standardized Coefficients",
       positive_color="#2a7f62", negative_color="#c0392b",
       template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/coefficients/standardized_coefficient_plot_interactive.png" alt="standardized_coefficient_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
