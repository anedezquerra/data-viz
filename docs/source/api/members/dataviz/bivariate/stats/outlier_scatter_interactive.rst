dataviz.bivariate.stats.outlier_scatter_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: outlier_scatter_interactive

Use case
--------

Use to flag unusual points in a two-variable relationship using z-score or IQR rules before fitting models.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.stats import outlier_scatter_interactive

   rng = np.random.default_rng(42)
   n = 90
   sessions = pd.Series(rng.normal(loc=30.0, scale=6.0, size=n), name="Sessions per month")
   orders = pd.Series(5.0 + 0.4 * sessions + rng.normal(loc=0.0, scale=2.0, size=n), name="Orders")
   orders.iloc[[7, 33, 71]] = [40.0, 2.0, 45.0]

   fig = outlier_scatter_interactive(
       sessions,
       orders,
       method="iqr",
       threshold=1.5,
       title="Customer Activity Outliers",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/outlier_scatter_interactive.png" alt="outlier_scatter_interactive example output"><figcaption>Example output</figcaption></figure></div>
