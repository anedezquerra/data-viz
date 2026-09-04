dataviz.bivariate.stats.lag_plot_interactive
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: lag_plot_interactive

Use case
--------

Use to check for delayed or leading-lag relationships between two ordered series, such as time-shifted signals.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.stats import lag_plot_interactive

   rng = np.random.default_rng(42)
   n = 100
   noise = rng.normal(loc=0.0, scale=1.0, size=n)
   flow = pd.Series(np.zeros(n), name="River flow (m3/s)")
   for i in range(1, n):
       flow.iloc[i] = 0.85 * flow.iloc[i - 1] + noise[i]

   fig = lag_plot_interactive(
       flow,
       flow,
       lag=1,
       title="River Flow Lag-1 Autocorrelation",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/lag_plot_interactive.png" alt="lag_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
