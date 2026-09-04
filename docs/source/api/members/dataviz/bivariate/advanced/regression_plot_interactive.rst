dataviz.bivariate.advanced.regression_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: regression_plot_interactive

Use case
--------

Use to overlay a polynomial trend line on a scatter plot when assessing whether a simple curve fits the relationship.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.advanced import regression_plot_interactive

   rng = np.random.default_rng(42)
   n = 50
   spend = pd.Series(rng.uniform(low=5.0, high=100.0, size=n), name="Marketing spend (k USD)")
   revenue = pd.Series(
       50.0 + 3.2 * spend - 0.015 * spend**2 + rng.normal(loc=0.0, scale=18.0, size=n),
       name="Revenue (k USD)",
   )

   fig = regression_plot_interactive(
       spend,
       revenue,
       degree=2,
       title="Revenue Response to Marketing Spend",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/regression_plot_interactive.png" alt="regression_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
