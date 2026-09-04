dataviz.regression.mixed_effects.random_intercept_slope_scatter_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.mixed_effects</p></div>

.. currentmodule:: dataviz.regression.mixed_effects

.. autofunction:: random_intercept_slope_scatter_static

Use case
--------

Use to check whether groups with higher random intercepts also show stronger or weaker random slopes.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.mixed_effects import random_intercept_slope_scatter_static

   rng = np.random.default_rng(42)
   schools = pd.Series([f"School {s:02d}" for s in range(1, 21)], name="school")
   random_intercepts = pd.Series(rng.normal(0.0, 2.5, size=20), name="intercept")
   random_slopes = pd.Series(
       -0.4 * random_intercepts + rng.normal(0.0, 0.6, size=20), name="slope"
   )

   ax = random_intercept_slope_scatter_static(
       random_intercepts, random_slopes,
       title="Education study: intercept vs slope per school",
       color="#6a4c93", theme="minimal",
   )
   ax.set_xlabel("Random intercept (baseline score)")
   ax.set_ylabel("Random slope (gain per week)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/mixed_effects/random_intercept_slope_scatter_static.png" alt="random_intercept_slope_scatter_static example output"><figcaption>Example output</figcaption></figure></div>
