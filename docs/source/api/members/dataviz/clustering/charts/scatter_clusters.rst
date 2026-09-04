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
   centers = [(2.0, 2.0), (8.0, 3.0), (5.0, 9.0)]
   points = [rng.normal(loc=c, scale=0.9, size=(30, 2)) for c in centers]
   data = np.vstack(points)
   labels = np.repeat([0, 1, 2], 30)

   ax = scatter_clusters(data[:, 0], data[:, 1], labels, title="Customer Segment Clusters")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/clustering/charts/scatter_clusters.png" alt="scatter_clusters example output"><figcaption>Example output</figcaption></figure></div>
