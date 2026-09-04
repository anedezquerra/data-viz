dataviz.regression.mixed_effects.random_effect_caterpillar_interactive
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.mixed_effects</p></div>

.. currentmodule:: dataviz.regression.mixed_effects

.. autofunction:: random_effect_caterpillar_interactive

Use case
--------

Use to rank group-level random effects with standard-error bars and see which groups differ significantly from zero.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.mixed_effects import random_effect_caterpillar_interactive

   rng = np.random.default_rng(42)
   clinics = pd.Series([f"Clinic {c:02d}" for c in range(1, 16)], name="clinic")
   random_effects = pd.Series(rng.normal(0.0, 1.2, size=15), name="intercept_shift")
   std_errors = pd.Series(rng.uniform(0.25, 0.6, size=15), name="se")

   fig = random_effect_caterpillar_interactive(
       clinics, random_effects, std_errors=std_errors,
       title="Clinical trial: random intercepts by site",
       color="#2a6f97", template="plotly_white", height=700,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/mixed_effects/random_effect_caterpillar_interactive.png" alt="random_effect_caterpillar_interactive example output"><figcaption>Example output</figcaption></figure></div>
