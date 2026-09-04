dataviz.clustering.charts.scatter_clusters
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.clustering.charts</p></div>

.. currentmodule:: dataviz.clustering.charts

.. autofunction:: scatter_clusters

Use case
--------

Use to sanity-check clustering results by coloring points by cluster label in a two-dimensional view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.clustering.charts import scatter_clusters

   rng = np.random.default_rng(42)
   x = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
   y = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
   labels = np.repeat([0, 1], 20)

   ax = scatter_clusters(x, y, labels, title="Cluster visualization")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/clustering/charts/scatter_clusters.png" alt="scatter_clusters example output"><figcaption>Example output</figcaption></figure></div>
