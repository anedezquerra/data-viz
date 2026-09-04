dataviz.bivariate.line.line_plot_interactive
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.line</p></div>

.. currentmodule:: dataviz.bivariate.line

.. autofunction:: line_plot_interactive

Use case
--------

Use to show how a numeric variable changes across an ordered axis such as time or sequence index.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.line import line_plot_interactive

   rng = np.random.default_rng(42)
   df = pd.DataFrame({
       "Week": np.arange(1, 53),
       "Active users": 10000.0 + np.cumsum(rng.normal(loc=120.0, scale=300.0, size=52)),
   })

   fig = line_plot_interactive(
       "Week",
       "Active users",
       data=df,
       title="Weekly Active Users",
       mode="lines+markers",
       rolling_window=4,
       hline=10000.0,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/line/line_plot_interactive.png" alt="line_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
