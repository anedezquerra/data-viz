dataviz.bivariate.categorical.box_by_category_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: box_by_category_interactive

Use case
--------

Use to compare the spread, median, and outliers of a numeric variable across categories.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.categorical import box_by_category_interactive

   rng = np.random.default_rng(42)
   n = 120
   plan = pd.Series(np.repeat(["Basic", "Pro", "Enterprise"], n // 3), name="Plan")
   support_hours = pd.Series(
       np.concatenate([
           rng.normal(loc=2.0, scale=0.8, size=n // 3),
           rng.normal(loc=6.0, scale=1.5, size=n // 3),
           rng.normal(loc=14.0, scale=3.0, size=n // 3),
       ]),
       name="Support hours per month",
   )

   fig = box_by_category_interactive(
       plan,
       support_hours,
       title="Support Usage by Subscription Plan",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/box_by_category_interactive.png" alt="box_by_category_interactive example output"><figcaption>Example output</figcaption></figure></div>
