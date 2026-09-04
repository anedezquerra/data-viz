dataviz.bivariate.stats.quantile_bin_plot_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: quantile_bin_plot_interactive

Use case
--------

Use to summarize how a y statistic, mean or median, varies across quantile bins of x for a robust trend view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.stats import quantile_bin_plot_interactive

   rng = np.random.default_rng(42)
   n = 200
   income = pd.Series(rng.lognormal(mean=10.8, sigma=0.4, size=n), name="Annual income (USD)")
   savings_rate = pd.Series(
       5.0 + 0.0001 * income + rng.normal(loc=0.0, scale=3.0, size=n),
       name="Savings rate (%)",
   )

   fig = quantile_bin_plot_interactive(
       income,
       savings_rate,
       q=8,
       statistic="median",
       title="Median Savings Rate by Income Decile",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/quantile_bin_plot_interactive.png" alt="quantile_bin_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
