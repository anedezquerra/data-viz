dataviz.regression.multicollinearity.correlation_heatmap_with_clustering_static
===============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: correlation_heatmap_with_clustering_static

Use case
--------

Use to surface clusters of highly correlated predictors so redundant features can be dropped or combined.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.multicollinearity import correlation_heatmap_with_clustering_static

   rng = np.random.default_rng(42)
   x1 = rng.normal(0.0, 1.0, size=60)
   X = np.column_stack([x1, 0.9 * x1 + rng.normal(0.0, 0.1, size=60), rng.normal(0.0, 1.0, size=60)])

   ax = correlation_heatmap_with_clustering_static(X, feature_names=["x1", "x2", "x3"])
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/multicollinearity/correlation_heatmap_with_clustering_static.png" alt="correlation_heatmap_with_clustering_static example output"><figcaption>Example output</figcaption></figure></div>
