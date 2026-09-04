dataviz.classification.pr_curve.precision_recall_curve_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.pr_curve</p></div>

.. currentmodule:: dataviz.classification.pr_curve

.. autofunction:: precision_recall_curve_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.pr_curve import precision_recall_curve_static

   cm = np.array([[32, 4], [5, 29]])
   fpr = np.array([0.0, 0.1, 0.3, 1.0])
   tpr = np.array([0.0, 0.7, 0.9, 1.0])
   precision = np.array([1.0, 0.86, 0.72])
   recall = np.array([0.2, 0.7, 1.0])

   ax = precision_recall_curve_static(precision, recall)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/pr_curve/precision_recall_curve_static.png" alt="precision_recall_curve_static example output"><figcaption>Example output</figcaption></figure></div>
