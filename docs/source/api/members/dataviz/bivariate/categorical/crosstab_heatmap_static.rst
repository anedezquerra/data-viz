dataviz.bivariate.categorical.crosstab_heatmap_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: crosstab_heatmap_static

Use case
--------

Use to spot associations between two categorical variables by mapping their contingency table to color intensity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.categorical import crosstab_heatmap_static

   rng = np.random.default_rng(42)
   n = 200
   channel = pd.Series(rng.choice(["Email", "Social", "Search", "Referral"], size=n), name="Channel")
   converted = pd.Series(rng.choice(["Converted", "Bounced"], size=n, p=[0.35, 0.65]), name="Outcome")

   ax = crosstab_heatmap_static(
       channel,
       converted,
       normalize="index",
       title="Conversion Rate by Channel",
       cmap="YlGn",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/crosstab_heatmap_static.png" alt="crosstab_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
