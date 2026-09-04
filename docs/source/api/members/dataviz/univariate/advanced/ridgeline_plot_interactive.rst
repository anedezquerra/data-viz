dataviz.univariate.advanced.ridgeline_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: ridgeline_plot_interactive

Use case
--------

Use to stack density curves for several numeric dataframe columns to compare distribution shapes across variables at a glance.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.advanced import ridgeline_plot_interactive

   # Weekly delivery times (days) for three regional warehouses
   rng = np.random.default_rng(42)
   deliveries = pd.DataFrame({
       "North": rng.normal(loc=3.1, scale=0.8, size=40),
       "Central": rng.normal(loc=2.6, scale=0.6, size=40),
       "South": rng.normal(loc=3.8, scale=1.0, size=40),
   })

   fig = ridgeline_plot_interactive(
       deliveries,
       title="Delivery Time by Warehouse",
       xlabel="Delivery Time (days)",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/ridgeline_plot_interactive.png" alt="ridgeline_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
