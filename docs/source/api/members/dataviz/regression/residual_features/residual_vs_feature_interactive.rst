dataviz.regression.residual_features.residual_vs_feature_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_features</p></div>

.. currentmodule:: dataviz.regression.residual_features

.. autofunction:: residual_vs_feature_interactive

Use case
--------

Use to check whether a single feature still carries structure the model missed; a curved trend in residuals vs that feature signals nonlinearity or a missing interaction.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.residual_features import residual_vs_feature_interactive

   rng = np.random.default_rng(42)
   n = 40
   listings = pd.DataFrame({
       "sqft": rng.uniform(800, 3600, n),
   })
   noise = rng.normal(0, 18, n)
   price = 60 + 0.22 * listings["sqft"] + 0.00003 * listings["sqft"] ** 2 + noise
   y_pred = 70 + 0.26 * listings["sqft"]  # linear model misses curvature

   fig = residual_vs_feature_interactive(
       listings["sqft"], price, y_pred,
       feature_name="Living area (sqft)",
       title="Home pricing model: residuals vs living area",
       trend_color="#e45756",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_features/residual_vs_feature_interactive.png" alt="residual_vs_feature_interactive example output"><figcaption>Example output</figcaption></figure></div>
