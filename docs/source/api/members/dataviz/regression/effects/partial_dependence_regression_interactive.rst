dataviz.regression.effects.partial_dependence_regression_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: partial_dependence_regression_interactive

Use case
--------

Use to show the marginal effect of one feature on the predicted target, averaged over all other features.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.effects import partial_dependence_regression_interactive

   grid = pd.Series(np.linspace(500, 4000, 25), name="sqft")
   pd_values = pd.Series(60 + 0.09 * grid + 12 * np.log(grid / 500),
                         name="pd_price_k")

   fig = partial_dependence_regression_interactive(
       grid, pd_values,
       title="Partial Dependence: Living Area on Price",
       feature_name="living area (sqft)", color="#1f6fb2",
       template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/partial_dependence_regression_interactive.png" alt="partial_dependence_regression_interactive example output"><figcaption>Example output</figcaption></figure></div>
