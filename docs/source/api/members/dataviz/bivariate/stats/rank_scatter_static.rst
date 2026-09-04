dataviz.bivariate.stats.rank_scatter_static
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: rank_scatter_static

Use case
--------

Use to compare the rank ordering of two variables when monotonic association matters more than raw values.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.stats import rank_scatter_static

   rng = np.random.default_rng(42)
   n = 50
   quality = pd.Series(rng.uniform(low=1.0, high=10.0, size=n), name="Quality score")
   satisfaction = pd.Series(0.8 * quality + rng.normal(loc=0.0, scale=1.5, size=n), name="Satisfaction score")

   ax = rank_scatter_static(
       quality,
       satisfaction,
       title="Rank Agreement: Quality vs Satisfaction",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/rank_scatter_static.png" alt="rank_scatter_static example output"><figcaption>Example output</figcaption></figure></div>
