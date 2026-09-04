dataviz.multivariate.heatmap.heatmap_static
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.heatmap</p></div>

.. currentmodule:: dataviz.multivariate.heatmap

.. autofunction:: heatmap_static

Use case
--------

Use to display a numeric matrix as color intensity when patterns across two dimensions matter.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.multivariate.heatmap import heatmap_static

   rng = np.random.default_rng(42)
   days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   hours = [f"{h}:00" for h in range(6, 22, 2)]
   traffic = rng.integers(50, 500, size=(len(days), len(hours))).astype(float)
   traffic[5:, :3] *= 0.4
   df = pd.DataFrame(traffic, index=days, columns=hours)

   ax = heatmap_static(
       df,
       title="Store Foot Traffic by Day and Hour",
       cmap="YlOrRd",
       fmt=".0f",
       linewidths=0.4,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/multivariate/heatmap/heatmap_static.png" alt="heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
