dataviz.multivariate.heatmap.heatmap_static
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.heatmap</p></div>

.. currentmodule:: dataviz.multivariate.heatmap

.. autofunction:: heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.multivariate.heatmap import heatmap_static

   rng = np.random.default_rng(42)
   df = pd.DataFrame({
       "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
       "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
       "Yield": rng.normal(loc=90.0, scale=3.0, size=30),
   })

   ax = heatmap_static(df, title="Process heatmap")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/multivariate/heatmap/heatmap_static.png" alt="heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
