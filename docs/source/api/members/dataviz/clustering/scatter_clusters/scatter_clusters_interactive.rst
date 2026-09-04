dataviz.clustering.scatter_clusters.scatter_clusters_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.clustering.scatter_clusters</p></div>

.. currentmodule:: dataviz.clustering.scatter_clusters

.. autofunction:: scatter_clusters_interactive

Use case
--------

Use to sanity-check clustering results by coloring points by cluster label in a two-dimensional view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.clustering.scatter_clusters import scatter_clusters_interactive

   rng = np.random.default_rng(42)
   x = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
   y = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
   labels = np.repeat([0, 1], 20)

   fig = scatter_clusters_interactive(x, y, labels, title="Cluster visualization")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/clustering/scatter_clusters/scatter_clusters_interactive.png" alt="scatter_clusters_interactive example output"><figcaption>Example output</figcaption></figure></div>
