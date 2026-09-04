dataviz.xai.local_more.prototype_criticism_grid_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: prototype_criticism_grid_interactive

Use case
--------

Use to contrast representative prototypes with atypical criticisms side by side, summarizing what is typical and what the model may mishandle.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.xai.local_more import prototype_criticism_grid_interactive

   rng = np.random.default_rng(42)
   cols = [
       "tenure_months", "monthly_charges", "num_support_calls",
       "avg_session_min", "late_payments", "age",
   ]
   prototypes = pd.DataFrame(
       np.array([
           [36, 65, 0, 42, 0, 45],
           [48, 82, 1, 35, 0, 52],
           [24, 55, 0, 50, 0, 31],
       ], dtype=float), columns=cols,
   )
   criticisms = pd.DataFrame(
       np.array([
           [2, 118, 7, 4, 4, 23],
           [60, 39, 5, 61, 3, 68],
       ], dtype=float), columns=cols,
   )
   fig = prototype_criticism_grid_interactive(
       prototypes, criticisms,
       title="Typical vs atypical retained customers (MMD critic)",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/prototype_criticism_grid_interactive.png" alt="prototype_criticism_grid_interactive example output"><figcaption>Example output</figcaption></figure></div>
