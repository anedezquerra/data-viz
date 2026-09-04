dataviz.multivariate.pairplot.pairplot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.pairplot</p></div>

.. currentmodule:: dataviz.multivariate.pairplot

.. autofunction:: pairplot_interactive

Use case
--------

Use to survey all pairwise relationships and marginal distributions among several variables in one grid.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.multivariate.pairplot import pairplot_interactive

   rng = np.random.default_rng(42)
   n = 80
   horsepower = rng.normal(loc=150.0, scale=30.0, size=n)
   df = pd.DataFrame({
       "Horsepower": horsepower,
       "Weight (kg)": 1200.0 + 3.0 * horsepower + rng.normal(loc=0.0, scale=100.0, size=n),
       "Fuel economy (mpg)": 45.0 - 0.08 * horsepower + rng.normal(loc=0.0, scale=2.0, size=n),
       "Price (k USD)": 15.0 + 0.12 * horsepower + rng.normal(loc=0.0, scale=3.0, size=n),
   })

   fig = pairplot_interactive(
       df,
       title="Vehicle Specs Pairplot",
       marker_size=5,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/multivariate/pairplot/pairplot_interactive.png" alt="pairplot_interactive example output"><figcaption>Example output</figcaption></figure></div>
