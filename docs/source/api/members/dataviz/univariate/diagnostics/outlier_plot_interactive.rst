dataviz.univariate.diagnostics.outlier_plot_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.diagnostics</p></div>

.. currentmodule:: dataviz.univariate.diagnostics

.. autofunction:: outlier_plot_interactive

Use case
--------

Use an index plot that flags univariate outliers to locate which observations sit outside expected bounds.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.diagnostics import outlier_plot_interactive

   # Daily website sessions with two traffic spikes from a campaign
   rng = np.random.default_rng(42)
   sessions = pd.Series(
       np.concatenate([
           rng.normal(loc=4200.0, scale=380.0, size=44),
           np.array([7200.0, 2300.0]),
       ]),
       name="daily_sessions",
   )

   fig = outlier_plot_interactive(
       sessions,
       method="iqr",
       multiplier=1.5,
       title="Daily Session Outlier Review",
       xlabel="Day Index",
       ylabel="Sessions",
       color="steelblue",
       outlier_color="crimson",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/diagnostics/outlier_plot_interactive.png" alt="outlier_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
