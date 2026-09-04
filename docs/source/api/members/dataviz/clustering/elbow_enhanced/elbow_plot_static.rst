dataviz.clustering.elbow_enhanced.elbow_plot_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.clustering.elbow_enhanced</p></div>

.. currentmodule:: dataviz.clustering.elbow_enhanced

.. autofunction:: elbow_plot_static

Use case
--------

Use when choosing k for k-means by looking for the bend where added clusters stop reducing inertia much.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.clustering.elbow_enhanced import elbow_plot_static

   n_clusters = np.arange(1, 11)
   inertias = np.array([520.0, 210.0, 120.0, 90.0, 74.0, 66.0, 61.0, 57.0, 54.0, 52.0])

   ax = elbow_plot_static(
       n_clusters,
       inertias,
       title="Customer Segmentation Elbow",
       color="teal",
       elbow_idx=2,
       elbow_color="crimson",
       grid=True,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/clustering/elbow_enhanced/elbow_plot_static.png" alt="elbow_plot_static example output"><figcaption>Example output</figcaption></figure></div>
