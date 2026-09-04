dataviz.regression.coefficients.coefficient_forest_plot_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.coefficients</p></div>

.. currentmodule:: dataviz.regression.coefficients

.. autofunction:: coefficient_forest_plot_interactive

Use case
--------

Use to show OLS coefficients with 95% confidence intervals so viewers can see which effects are statistically distinguishable from zero.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.coefficients import coefficient_forest_plot_interactive

   rng = np.random.default_rng(42)
   n = 30
   X = pd.DataFrame({
       "sqft_k": rng.uniform(0.8, 3.5, n),
       "bedrooms": rng.integers(1, 6, n).astype(float),
       "age_years": rng.uniform(0, 60, n),
   })
   y = pd.Series(80 + 120 * X["sqft_k"] + 8 * X["bedrooms"]
                 - 0.6 * X["age_years"] + rng.normal(0, 15, n),
                 name="price_k")

   fig = coefficient_forest_plot_interactive(X, y, feature_names=list(X.columns),
                                             include_intercept=True,
                                             title="Housing Price OLS: 95% CI Forest",
                                             color="#1f6fb2",
                                             template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/coefficients/coefficient_forest_plot_interactive.png" alt="coefficient_forest_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
