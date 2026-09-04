dataviz.regression.domain.price_elasticity_curve_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.domain</p></div>

.. currentmodule:: dataviz.regression.domain

.. autofunction:: price_elasticity_curve_interactive

Use case
--------

Use in pricing analysis to plot quantity versus price with an elasticity fit, showing how demand responds to price changes.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.domain import price_elasticity_curve_interactive

   rng = np.random.default_rng(42)
   price = pd.Series(rng.uniform(8, 30, 24), name="price_usd")
   quantity = pd.Series(900 * price ** -1.4 * rng.normal(1, 0.06, 24),
                        name="units_sold")
   fitted = 900 * price ** -1.4

   fig = price_elasticity_curve_interactive(price, quantity, fitted_curve=fitted,
                                            title="Snack Line: Price Elasticity Curve",
                                            color="#1f6fb2",
                                            template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/domain/price_elasticity_curve_interactive.png" alt="price_elasticity_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
