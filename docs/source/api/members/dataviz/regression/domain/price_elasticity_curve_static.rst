dataviz.regression.domain.price_elasticity_curve_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.domain</p></div>

.. currentmodule:: dataviz.regression.domain

.. autofunction:: price_elasticity_curve_static

Use case
--------

Use in pricing analysis to plot quantity versus price with an elasticity fit, showing how demand responds to price changes.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.domain import price_elasticity_curve_static

   rng = np.random.default_rng(42)
   price = pd.Series(rng.uniform(8, 30, 24), name="price_usd")
   quantity = pd.Series(900 * price ** -1.4 * rng.normal(1, 0.06, 24),
                        name="units_sold")
   fitted = 900 * price ** -1.4

   ax = price_elasticity_curve_static(price, quantity, fitted_curve=fitted,
                                      title="Snack Line: Price Elasticity Curve",
                                      color="#1f6fb2")
   ax.set_ylabel("Weekly units sold")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/domain/price_elasticity_curve_static.png" alt="price_elasticity_curve_static example output"><figcaption>Example output</figcaption></figure></div>
