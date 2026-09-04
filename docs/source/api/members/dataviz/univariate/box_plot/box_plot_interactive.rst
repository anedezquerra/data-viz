dataviz.univariate.box_plot.box_plot_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.box_plot</p></div>

.. currentmodule:: dataviz.univariate.box_plot

.. autofunction:: box_plot_interactive

Use case
--------

Use to summarize quartiles, spread, and outliers of a numeric variable with hover detail; DataFrame input draws one box per column.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.box_plot import box_plot_interactive

   # Daily household electricity consumption with a few heavy-usage days
   rng = np.random.default_rng(42)
   usage_kwh = pd.Series(
       np.concatenate([
           rng.normal(loc=18.0, scale=3.5, size=36),
           np.array([34.2, 37.8]),
       ]),
       name="usage_kwh",
   )

   fig = box_plot_interactive(
       usage_kwh,
       title="Daily Electricity Consumption",
       ylabel="Consumption (kWh)",
       marker_color="steelblue",
       boxmean=True,
       points="all",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/box_plot/box_plot_interactive.png" alt="box_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
