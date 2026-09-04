dataviz.bivariate.correlation.correlation_heatmap_interactive
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.correlation</p></div>

.. currentmodule:: dataviz.bivariate.correlation

.. autofunction:: correlation_heatmap_interactive

Use case
--------

Use to scan pairwise correlations among dataframe columns and quickly find strongly related variable pairs.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.correlation import correlation_heatmap_interactive

   rng = np.random.default_rng(42)
   n = 80
   speed = rng.normal(loc=120.0, scale=6.0, size=n)
   df = pd.DataFrame({
       "Speed": speed,
       "Pressure": 40.0 + 0.3 * speed + rng.normal(loc=0.0, scale=2.0, size=n),
       "Temperature": rng.normal(loc=180.0, scale=5.0, size=n),
       "Yield": 95.0 - 0.2 * speed + rng.normal(loc=0.0, scale=1.5, size=n),
   })

   fig = correlation_heatmap_interactive(
       df,
       method="spearman",
       mask_upper=True,
       title="Process Variable Correlations",
       colorscale="RdBu",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/correlation/correlation_heatmap_interactive.png" alt="correlation_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
