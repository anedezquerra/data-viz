dataviz.bivariate.advanced.hexbin_plot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: hexbin_plot_interactive

Use case
--------

Use when a scatter plot of a large dataset overplots, to see point density as hexagonal bins.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.advanced import hexbin_plot_interactive

   rng = np.random.default_rng(42)
   n = 2000
   load = pd.Series(rng.normal(loc=70.0, scale=8.0, size=n), name="Server load (%)")
   latency = pd.Series(20.0 + 0.8 * load + rng.normal(loc=0.0, scale=6.0, size=n), name="Latency (ms)")

   fig = hexbin_plot_interactive(
       load,
       latency,
       nbinsx=30,
       nbinsy=30,
       title="Latency vs Server Load Density",
       colorscale="Magma",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/hexbin_plot_interactive.png" alt="hexbin_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
