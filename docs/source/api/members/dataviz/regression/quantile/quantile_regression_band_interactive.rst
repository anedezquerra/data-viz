dataviz.regression.quantile.quantile_regression_band_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: quantile_regression_band_interactive

Use case
--------

Use to visualize fitted low/median/high quantile curves against the data when modeling more than the conditional mean.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.quantile import quantile_regression_band_interactive

   rng = np.random.default_rng(42)
   distance_km = pd.Series(rng.uniform(2, 60, 25).round(1), name="distance_km")
   delivery_min = pd.Series(
       8 + 1.6 * distance_km + rng.gamma(2.0, 3.0, 25), name="delivery_min"
   )
   q10 = 6 + 1.45 * distance_km
   q50 = 8 + 1.60 * distance_km
   q90 = 11 + 1.85 * distance_km

   fig = quantile_regression_band_interactive(
       distance_km, delivery_min, q10, q50, q90,
       title="Courier delivery time: 10/50/90% quantile band",
       color="#2a6f97", band_color="rgba(168,213,229,0.5)",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/quantile/quantile_regression_band_interactive.png" alt="quantile_regression_band_interactive example output"><figcaption>Example output</figcaption></figure></div>
