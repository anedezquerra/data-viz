dataviz.regression.multicollinearity.condition_index_plot_interactive
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: condition_index_plot_interactive

Use case
--------

Use to detect near-collinearity in the design matrix via condition indices, complementing per-feature VIF checks.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.multicollinearity import condition_index_plot_interactive

   rng = np.random.default_rng(42)
   n = 36
   engine_size = rng.normal(2.4, 0.6, n)
   vehicles = pd.DataFrame({
       "engine_l": engine_size,
       "horsepower": 95 * engine_size + rng.normal(0, 12, n),
       "weight_kg": 620 * engine_size + rng.normal(0, 90, n),
       "wheelbase_in": rng.normal(104, 6, n),
   })

   fig = condition_index_plot_interactive(
       vehicles, title="Fuel-efficiency model: condition indices",
       threshold=30.0, color="#ee854a", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/condition_index_plot_interactive.png" alt="condition_index_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
