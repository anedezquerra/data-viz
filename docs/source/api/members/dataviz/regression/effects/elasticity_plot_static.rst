dataviz.regression.effects.elasticity_plot_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: elasticity_plot_static

Use case
--------

Use to plot elasticity, the percent change in prediction per percent change in a feature, when scale-free sensitivity matters.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.effects import elasticity_plot_static

   price_grid = pd.Series(np.linspace(5, 40, 22), name="price_usd")
   elasticity = pd.Series(-1.8 + 0.9 * np.exp(-price_grid / 12),
                          name="elasticity")

   ax = elasticity_plot_static(price_grid, elasticity,
                               title="Own-Price Elasticity by Price Point",
                               feature_name="price (USD)", color="#1f6fb2")
   ax.axhline(-1.0, color="#c0392b", linestyle=":", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/elasticity_plot_static.png" alt="elasticity_plot_static example output"><figcaption>Example output</figcaption></figure></div>
