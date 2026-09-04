dataviz.regression.multicollinearity.vif_bar_interactive
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: vif_bar_interactive

Use case
--------

Use to flag predictors whose variance inflation factor exceeds a threshold before fitting a linear model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.multicollinearity import vif_bar_interactive

   rng = np.random.default_rng(42)
   n = 36
   living_area = rng.normal(1800, 400, n)
   housing = pd.DataFrame({
       "living_area_sqft": living_area,
       "bedrooms": np.clip(living_area / 450 + rng.normal(0, 0.4, n), 1, 6),
       "bathrooms": np.clip(living_area / 700 + rng.normal(0, 0.3, n), 1, 4),
       "lot_size_sqft": rng.normal(6000, 1500, n),
       "age_years": rng.uniform(0, 60, n),
   })

   fig = vif_bar_interactive(
       housing, feature_names=list(housing.columns),
       title="Housing price model: variance inflation factors",
       threshold=5.0, color="#4878d0", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/vif_bar_interactive.png" alt="vif_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
