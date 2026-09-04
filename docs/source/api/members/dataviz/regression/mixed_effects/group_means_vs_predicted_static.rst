dataviz.regression.mixed_effects.group_means_vs_predicted_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.mixed_effects</p></div>

.. currentmodule:: dataviz.regression.mixed_effects

.. autofunction:: group_means_vs_predicted_static

Use case
--------

Use to compare observed group means against mixed-model predicted means to spot groups the model fits poorly.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.mixed_effects import group_means_vs_predicted_static

   rng = np.random.default_rng(42)
   lines = pd.Series([f"Line {c}" for c in "ABCDEFGHIJ"], name="line")
   observed = pd.Series(rng.normal(92.0, 4.0, size=10).round(2), name="observed_yield")
   predicted = pd.Series(observed + rng.normal(0.0, 1.5, size=10), name="predicted_yield")

   ax = group_means_vs_predicted_static(
       lines, observed, predicted,
       title="Manufacturing yield: observed vs mixed-model predicted",
       obs_color="#1b9e77", pred_color="#d95f02", theme="minimal",
   )
   ax.set_ylabel("Mean yield (%)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/mixed_effects/group_means_vs_predicted_static.png" alt="group_means_vs_predicted_static example output"><figcaption>Example output</figcaption></figure></div>
