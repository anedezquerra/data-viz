dataviz.univariate.dashboard.univariate_analysis_dashboard_interactive
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.dashboard</p></div>

.. currentmodule:: dataviz.univariate.dashboard

.. autofunction:: univariate_analysis_dashboard_interactive

Use case
--------

Use to get a multi-panel interactive overview of one variable combining several univariate views in a single figure.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.dashboard import univariate_analysis_dashboard_interactive

   # Quarterly revenue per store for a regional retail chain
   rng = np.random.default_rng(42)
   revenue_k = pd.Series(
       np.round(rng.lognormal(mean=11.2, sigma=0.4, size=46) / 1000.0, 1),
       name="revenue_kusd",
   )

   fig = univariate_analysis_dashboard_interactive(
       revenue_k,
       bins=12,
       title="Store Revenue Profile (USD thousands)",
       color="steelblue",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/dashboard/univariate_analysis_dashboard_interactive.png" alt="univariate_analysis_dashboard_interactive example output"><figcaption>Example output</figcaption></figure></div>
