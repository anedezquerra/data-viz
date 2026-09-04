dataviz.classification.multiclass.multiclass_roc_curve_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: multiclass_roc_curve_static

Use case
--------

Use when evaluating a multiclass classifier one class at a time; plots one-vs-rest ROC per class with optional macro average and random baseline.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass import multiclass_roc_curve_static

   curves = {
       "Class 0": (np.array([0.0, 0.1, 0.3, 1.0]), np.array([0.0, 0.8, 0.9, 1.0])),
       "Class 1": (np.array([0.0, 0.2, 0.4, 1.0]), np.array([0.0, 0.6, 0.8, 1.0])),
       "Class 2": (np.array([0.0, 0.3, 0.5, 1.0]), np.array([0.0, 0.5, 0.75, 1.0])),
   }

   ax = multiclass_roc_curve_static(curves)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass/multiclass_roc_curve_static.png" alt="multiclass_roc_curve_static example output"><figcaption>Example output</figcaption></figure></div>
