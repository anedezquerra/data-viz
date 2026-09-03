dataviz.clustering.dendrogram.dendrogram_static
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.clustering.dendrogram</p></div>

.. currentmodule:: dataviz.clustering.dendrogram

.. autofunction:: dendrogram_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.clustering.dendrogram import dendrogram_static

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")
   labels = np.array([0, 0, 1, 1])
   k_values = np.array([1, 2, 3, 4])
   inertias = np.array([10.0, 4.2, 2.6, 2.1])
   linkage_matrix = np.array([[0, 1, 0.3, 2], [2, 3, 0.4, 2], [4, 5, 3.0, 4]])

   ax = dendrogram_static(linkage_matrix)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/clustering/dendrogram/dendrogram_static.png" alt="dendrogram_static example output"><figcaption>Example output</figcaption></figure></div>
