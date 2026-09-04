dataviz.regression.mixed_effects.random_effect_caterpillar_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.mixed_effects</p></div>

.. currentmodule:: dataviz.regression.mixed_effects

.. autofunction:: random_effect_caterpillar_static

Use case
--------

Use to rank group-level random effects with standard-error bars and see which groups differ significantly from zero.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.mixed_effects import random_effect_caterpillar_static

   rng = np.random.default_rng(42)
   clinics = pd.Series([f"Clinic {c:02d}" for c in range(1, 16)], name="clinic")
   random_effects = pd.Series(rng.normal(0.0, 1.2, size=15), name="intercept_shift")
   std_errors = pd.Series(rng.uniform(0.25, 0.6, size=15), name="se")

   ax = random_effect_caterpillar_static(
       clinics, random_effects, std_errors=std_errors,
       title="Clinical trial: random intercepts by site",
       color="#2a6f97", theme="minimal",
   )
   ax.set_xlabel("Treatment effect shift (mmHg)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/mixed_effects/random_effect_caterpillar_static.png" alt="random_effect_caterpillar_static example output"><figcaption>Example output</figcaption></figure></div>
