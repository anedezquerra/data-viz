dataviz.bivariate.trends.step_plot_interactive
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.trends</p></div>

.. currentmodule:: dataviz.bivariate.trends

.. autofunction:: step_plot_interactive

Use case
--------

Use for values that change discretely at known points, such as cumulative counts or rate changes over time.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.trends import step_plot_interactive

   quarter = pd.Series(np.arange(1, 13), name="Quarter")
   price = pd.Series(
       [9.99, 9.99, 10.49, 10.49, 10.49, 10.99, 10.99, 11.49, 11.49, 11.49, 11.99, 11.99],
       name="Subscription price (USD)",
   )

   fig = step_plot_interactive(
       quarter,
       price,
       shape="hv",
       title="Subscription Price Changes Over Time",
       color="darkorange",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/trends/step_plot_interactive.png" alt="step_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
