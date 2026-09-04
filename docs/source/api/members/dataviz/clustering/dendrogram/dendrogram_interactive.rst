dataviz.clustering.dendrogram.dendrogram_interactive
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.clustering.dendrogram</p></div>

.. currentmodule:: dataviz.clustering.dendrogram

.. autofunction:: dendrogram_interactive

Use case
--------

Use to inspect hierarchical clustering merges and decide where to cut the tree into flat clusters.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from scipy.cluster.hierarchy import linkage
   from dataviz.clustering.dendrogram import dendrogram_interactive

   rng = np.random.default_rng(42)
   data = np.vstack([
       rng.normal(loc=0.0, scale=0.8, size=(10, 2)),
       rng.normal(loc=5.0, scale=0.8, size=(10, 2)),
       rng.normal(loc=[5.0, 0.0], scale=0.8, size=(10, 2)),
   ])
   linkage_matrix = linkage(data, method="ward")
   labels = [f"Sensor {i + 1}" for i in range(len(data))]

   fig = dendrogram_interactive(
       linkage_matrix,
       labels=labels,
       title="Sensor Network Dendrogram",
       color_threshold=4.0,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/clustering/dendrogram/dendrogram_interactive.png" alt="dendrogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
