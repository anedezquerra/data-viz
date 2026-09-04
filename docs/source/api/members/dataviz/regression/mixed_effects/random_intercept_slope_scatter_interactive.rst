dataviz.regression.mixed_effects.random_intercept_slope_scatter_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.mixed_effects</p></div>

.. currentmodule:: dataviz.regression.mixed_effects

.. autofunction:: random_intercept_slope_scatter_interactive

Use case
--------

Use to check whether groups with higher random intercepts also show stronger or weaker random slopes.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.mixed_effects import random_intercept_slope_scatter_interactive

   rng = np.random.default_rng(42)
   schools = pd.Series([f"School {s:02d}" for s in range(1, 21)], name="school")
   random_intercepts = pd.Series(rng.normal(0.0, 2.5, size=20), name="intercept")
   random_slopes = pd.Series(
       -0.4 * random_intercepts + rng.normal(0.0, 0.6, size=20), name="slope"
   )

   fig = random_intercept_slope_scatter_interactive(
       random_intercepts, random_slopes,
       title="Education study: intercept vs slope per school",
       color="#6a4c93", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/mixed_effects/random_intercept_slope_scatter_interactive.png" alt="random_intercept_slope_scatter_interactive example output"><figcaption>Example output</figcaption></figure></div>
