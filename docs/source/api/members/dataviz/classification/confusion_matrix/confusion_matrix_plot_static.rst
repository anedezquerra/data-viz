dataviz.classification.confusion_matrix.confusion_matrix_plot_static
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.confusion_matrix</p></div>

.. currentmodule:: dataviz.classification.confusion_matrix

.. autofunction:: confusion_matrix_plot_static

Use case
--------

Use for a publication-style confusion matrix heatmap with counts, labels and colorbar.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.confusion_matrix import confusion_matrix_plot_static

   cm = np.array([[32, 4], [5, 29]])
   fpr = np.array([0.0, 0.1, 0.3, 1.0])
   tpr = np.array([0.0, 0.7, 0.9, 1.0])
   precision = np.array([1.0, 0.86, 0.72])
   recall = np.array([0.2, 0.7, 1.0])

   ax = confusion_matrix_plot_static(cm)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/confusion_matrix/confusion_matrix_plot_static.png" alt="confusion_matrix_plot_static example output"><figcaption>Example output</figcaption></figure></div>
