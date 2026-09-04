dataviz.bivariate.categorical.violin_by_category_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: violin_by_category_interactive

Use case
--------

Use when box plots hide bimodal or skewed shapes and you need the full distribution per category.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.categorical import violin_by_category_interactive

   rng = np.random.default_rng(42)
   n = 150
   shift = pd.Series(np.repeat(["Morning", "Afternoon", "Night"], n // 3), name="Shift")
   cycle_time = pd.Series(
       np.concatenate([
           rng.normal(loc=45.0, scale=4.0, size=n // 3),
           rng.normal(loc=52.0, scale=6.0, size=n // 3),
           rng.normal(loc=49.0, scale=3.0, size=n // 3),
       ]),
       name="Cycle time (s)",
   )

   fig = violin_by_category_interactive(
       shift,
       cycle_time,
       title="Cycle Time Shape by Shift",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/violin_by_category_interactive.png" alt="violin_by_category_interactive example output"><figcaption>Example output</figcaption></figure></div>
