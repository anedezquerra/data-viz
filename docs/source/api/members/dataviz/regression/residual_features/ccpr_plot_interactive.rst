dataviz.regression.residual_features.ccpr_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_features</p></div>

.. currentmodule:: dataviz.regression.residual_features

.. autofunction:: ccpr_plot_interactive

Use case
--------

Use to judge where the linear component of one predictor fits well and where residuals spread out, helping spot nonlinearity or heteroscedasticity per feature.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.residual_features import ccpr_plot_interactive

   rng = np.random.default_rng(42)
   n = 35
   cars = pd.DataFrame({
       "horsepower": rng.uniform(90, 320, n),
       "weight_kg": rng.uniform(900, 2100, n),
       "age_years": rng.uniform(0, 12, n),
   })
   mpg = (52 - 0.045 * cars["horsepower"] - 0.008 * cars["weight_kg"]
          - 0.6 * cars["age_years"] + rng.normal(0, 1.5, n))

   fig = ccpr_plot_interactive(
       cars, mpg, feature_index=1, feature_name="weight_kg",
       title="Fuel economy study: CCPR for vehicle weight",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_features/ccpr_plot_interactive.png" alt="ccpr_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
