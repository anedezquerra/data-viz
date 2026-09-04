dataviz.regression.multicollinearity.eigenvalue_scree_predictors_interactive
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: eigenvalue_scree_predictors_interactive

Use case
--------

Use to see how much predictor variance concentrates in a few components, a sign of multicollinearity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.multicollinearity import eigenvalue_scree_predictors_interactive

   rng = np.random.default_rng(42)
   n = 40
   size = rng.normal(2000, 500, n)
   homes = pd.DataFrame({
       "sqft": size,
       "bedrooms": size / 480 + rng.normal(0, 0.4, n),
       "bathrooms": size / 750 + rng.normal(0, 0.3, n),
       "garage_cars": np.clip(size / 900 + rng.normal(0, 0.3, n), 0, 4),
       "lot_sqft": rng.normal(7000, 1800, n),
   })

   fig = eigenvalue_scree_predictors_interactive(
       homes, title="Home appraisal model: predictor eigenvalue scree",
       color="#6acc64", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/eigenvalue_scree_predictors_interactive.png" alt="eigenvalue_scree_predictors_interactive example output"><figcaption>Example output</figcaption></figure></div>
