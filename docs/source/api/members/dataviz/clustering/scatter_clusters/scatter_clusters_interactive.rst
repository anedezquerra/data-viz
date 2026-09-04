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
   centers = [(2.0, 2.0), (8.0, 3.0), (5.0, 9.0)]
   points = [rng.normal(loc=c, scale=0.9, size=(30, 2)) for c in centers]
   data = np.vstack(points)
   labels = np.repeat([0, 1, 2], 30)

   fig = scatter_clusters_interactive(
       data[:, 0],
       data[:, 1],
       labels,
       title="Customer Segment Clusters",
       xlabel="Annual spending (k USD)",
       ylabel="Visit frequency",
       show_centroids=True,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/clustering/scatter_clusters/scatter_clusters_interactive.png" alt="scatter_clusters_interactive example output"><figcaption>Example output</figcaption></figure></div>
