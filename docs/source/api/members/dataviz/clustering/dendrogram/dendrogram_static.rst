dataviz.clustering.dendrogram.dendrogram_static
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.clustering.dendrogram</p></div>

.. currentmodule:: dataviz.clustering.dendrogram

.. autofunction:: dendrogram_static

Use case
--------

Use to inspect hierarchical clustering merges and decide where to cut the tree into flat clusters.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from scipy.cluster.hierarchy import linkage
   from dataviz.clustering.dendrogram import dendrogram_static

   rng = np.random.default_rng(42)
   data = np.vstack([
       rng.normal(loc=0.0, scale=0.8, size=(10, 2)),
       rng.normal(loc=5.0, scale=0.8, size=(10, 2)),
       rng.normal(loc=[5.0, 0.0], scale=0.8, size=(10, 2)),
   ])
   linkage_matrix = linkage(data, method="ward")
   labels = [f"Sensor {i + 1}" for i in range(len(data))]

   ax = dendrogram_static(
       linkage_matrix,
       labels=labels,
       title="Sensor Network Dendrogram",
       color_threshold=4.0,
       leaf_font_size=9,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/clustering/dendrogram/dendrogram_static.png" alt="dendrogram_static example output"><figcaption>Example output</figcaption></figure></div>
