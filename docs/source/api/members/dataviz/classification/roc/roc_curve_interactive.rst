dataviz.classification.roc.roc_curve_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.roc</p></div>

.. currentmodule:: dataviz.classification.roc

.. autofunction:: roc_curve_interactive

Use case
--------

Use to assess a binary classifier from precomputed fpr/tpr arrays, with optional AUC label and random-chance reference line.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.roc import roc_curve_interactive

   cm = np.array([[32, 4], [5, 29]])
   fpr = np.array([0.0, 0.1, 0.3, 1.0])
   tpr = np.array([0.0, 0.7, 0.9, 1.0])
   precision = np.array([1.0, 0.86, 0.72])
   recall = np.array([0.2, 0.7, 1.0])

   fig = roc_curve_interactive(fpr, tpr)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/roc/roc_curve_interactive.png" alt="roc_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
