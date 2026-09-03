dataviz.regression.multicollinearity.correlation_heatmap_with_clustering_interactive
====================================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.multicollinearity</p></div>

.. currentmodule:: dataviz.regression.multicollinearity

.. autofunction:: correlation_heatmap_with_clustering_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.multicollinearity import correlation_heatmap_with_clustering_interactive

   rng = np.random.default_rng(42)
   x1 = rng.normal(0.0, 1.0, size=60)
   X = np.column_stack([x1, 0.9 * x1 + rng.normal(0.0, 0.1, size=60), rng.normal(0.0, 1.0, size=60)])

   fig = correlation_heatmap_with_clustering_interactive(X, feature_names=["x1", "x2", "x3"])
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/multicollinearity/correlation_heatmap_with_clustering_interactive.png" alt="correlation_heatmap_with_clustering_interactive example output"><figcaption>Example output</figcaption></figure></div>
