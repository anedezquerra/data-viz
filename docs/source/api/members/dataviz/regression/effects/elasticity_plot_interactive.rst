dataviz.regression.effects.elasticity_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: elasticity_plot_interactive

Use case
--------

Use to plot elasticity, the percent change in prediction per percent change in a feature, when scale-free sensitivity matters.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.effects import elasticity_plot_interactive

   price_grid = pd.Series(np.linspace(5, 40, 22), name="price_usd")
   elasticity = pd.Series(-1.8 + 0.9 * np.exp(-price_grid / 12),
                          name="elasticity")

   fig = elasticity_plot_interactive(price_grid, elasticity,
                                     title="Own-Price Elasticity by Price Point",
                                     feature_name="price (USD)", color="#1f6fb2",
                                     template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/elasticity_plot_interactive.png" alt="elasticity_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
