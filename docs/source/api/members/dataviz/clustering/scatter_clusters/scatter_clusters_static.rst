dataviz.clustering.scatter_clusters.scatter_clusters_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.clustering.scatter_clusters</p></div>

.. currentmodule:: dataviz.clustering.scatter_clusters

.. autofunction:: scatter_clusters_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.clustering.scatter_clusters import scatter_clusters_static

   rng = np.random.default_rng(42)
   x = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
   y = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
   labels = np.repeat([0, 1], 20)

   ax = scatter_clusters_static(x, y, labels, title="Cluster visualization")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
