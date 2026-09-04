dataviz.classification.multiclass.roc_curve_comparison_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: roc_curve_comparison_static

Use case
--------

Use to overlay ROC curves from several candidate models on one axes and pick the best discriminator by AUC.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass import roc_curve_comparison_static

   models = {
       "Logistic regression": (np.array([0.0, 0.1, 0.3, 1.0]), np.array([0.0, 0.7, 0.9, 1.0])),
       "Random forest": (np.array([0.0, 0.05, 0.2, 1.0]), np.array([0.0, 0.8, 0.95, 1.0])),
       "Gradient boosting": (np.array([0.0, 0.08, 0.25, 1.0]), np.array([0.0, 0.75, 0.92, 1.0])),
   }

   ax = roc_curve_comparison_static(models)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass/roc_curve_comparison_static.png" alt="roc_curve_comparison_static example output"><figcaption>Example output</figcaption></figure></div>
