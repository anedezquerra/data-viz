dataviz.multivariate.parallel.parallel_coordinates_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.parallel</p></div>

.. currentmodule:: dataviz.multivariate.parallel

.. autofunction:: parallel_coordinates_interactive

Use case
--------

Use to compare many observations across several numeric variables at once and spot multivariate outliers or clusters.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.multivariate.parallel import parallel_coordinates_interactive

   rng = np.random.default_rng(42)
   n = 60
   df = pd.DataFrame({
       "Battery (h)": rng.normal(loc=12.0, scale=2.0, size=n),
       "Weight (g)": rng.normal(loc=180.0, scale=25.0, size=n),
       "Screen (in)": rng.normal(loc=6.1, scale=0.4, size=n),
       "Price (USD)": rng.normal(loc=700.0, scale=150.0, size=n),
       "Rating": rng.uniform(low=3.0, high=5.0, size=n),
   })

   fig = parallel_coordinates_interactive(
       df,
       title="Smartphone Model Comparison",
       color_col="Rating",
       colorscale="Viridis",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/multivariate/parallel/parallel_coordinates_interactive.png" alt="parallel_coordinates_interactive example output"><figcaption>Example output</figcaption></figure></div>
