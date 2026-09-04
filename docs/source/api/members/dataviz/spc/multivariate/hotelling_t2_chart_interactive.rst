dataviz.spc.multivariate.hotelling_t2_chart_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.multivariate</p></div>

.. currentmodule:: dataviz.spc.multivariate

.. autofunction:: hotelling_t2_chart_interactive

Use case
--------

Use to chart Hotelling T-squared scores against a control limit to detect multivariate shifts in correlated process variables.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.spc.multivariate import hotelling_t2_chart_interactive

   rng = np.random.default_rng(42)
   # 30 hourly readings of correlated reactor variables
   temp = rng.normal(180.0, 1.5, size=30)
   pressure = 4.0 + 0.02 * (temp - 180.0) + rng.normal(0.0, 0.05, size=30)
   flow = rng.normal(12.0, 0.4, size=30)
   temp[24] = 185.8  # heater excursion
   df = pd.DataFrame({"temp": temp, "pressure": pressure, "flow": flow})

   fig = hotelling_t2_chart_interactive(df, limit_quantile=0.99, title="Reactor Hotelling T-squared Chart")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/multivariate/hotelling_t2_chart_interactive.png" alt="hotelling_t2_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
