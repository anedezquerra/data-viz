dataviz.classification.multiclass.pr_curve_comparison_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: pr_curve_comparison_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass import pr_curve_comparison_static

   models = {
       "Logistic regression": (np.array([0.0, 0.5, 1.0]), np.array([0.85, 0.8, 0.55])),
       "Random forest": (np.array([0.0, 0.5, 1.0]), np.array([0.9, 0.88, 0.65])),
       "Gradient boosting": (np.array([0.0, 0.5, 1.0]), np.array([0.88, 0.84, 0.6])),
   }

   ax = pr_curve_comparison_static(models)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass/pr_curve_comparison_static.png" alt="pr_curve_comparison_static example output"><figcaption>Example output</figcaption></figure></div>
