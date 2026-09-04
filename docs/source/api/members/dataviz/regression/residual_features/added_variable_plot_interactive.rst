dataviz.regression.residual_features.added_variable_plot_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_features</p></div>

.. currentmodule:: dataviz.regression.residual_features

.. autofunction:: added_variable_plot_interactive

Use case
--------

Use to decide whether adding a candidate predictor helps an OLS model; a strong slope in the partial-regression scatter means the feature adds information beyond the others.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.residual_features import added_variable_plot_interactive

   rng = np.random.default_rng(42)
   n = 35
   cars = pd.DataFrame({
       "horsepower": rng.uniform(90, 320, n),
       "weight_kg": rng.uniform(900, 2100, n),
       "age_years": rng.uniform(0, 12, n),
   })
   mpg = (52 - 0.045 * cars["horsepower"] - 0.008 * cars["weight_kg"]
          - 0.6 * cars["age_years"] + rng.normal(0, 1.5, n))

   fig = added_variable_plot_interactive(
       cars, mpg, feature_index=2, feature_name="age_years",
       title="Fuel economy study: added-variable plot for car age",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_features/added_variable_plot_interactive.png" alt="added_variable_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
