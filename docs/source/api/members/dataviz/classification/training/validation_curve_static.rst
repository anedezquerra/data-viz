dataviz.classification.training.validation_curve_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.training</p></div>

.. currentmodule:: dataviz.classification.training

.. autofunction:: validation_curve_static

Use case
--------

Use to tune a hyperparameter; plots train and validation score means with std bands over the swept values.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.training import validation_curve_static

   rng = np.random.default_rng(42)
   # random-forest depth sweep with 5-fold CV on a churn dataset
   depths = np.array([2, 4, 6, 8, 10, 12])
   train_scores = np.array([
       [0.71, 0.70, 0.72, 0.71, 0.70],
       [0.78, 0.77, 0.79, 0.78, 0.77],
       [0.85, 0.84, 0.86, 0.85, 0.84],
       [0.91, 0.90, 0.92, 0.91, 0.90],
       [0.95, 0.94, 0.96, 0.95, 0.94],
       [0.97, 0.96, 0.98, 0.97, 0.96],
   ])
   val_scores = np.array([
       [0.68, 0.67, 0.69, 0.68, 0.67],
       [0.74, 0.73, 0.75, 0.74, 0.72],
       [0.79, 0.78, 0.80, 0.79, 0.77],
       [0.81, 0.80, 0.82, 0.81, 0.79],
       [0.80, 0.79, 0.81, 0.80, 0.78],
       [0.78, 0.77, 0.79, 0.78, 0.76],
   ])

   ax = validation_curve_static(depths, train_scores, val_scores,
                                param_name="max_depth",
                                title="Churn RF: validation curve")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/training/validation_curve_static.png" alt="validation_curve_static example output"><figcaption>Example output</figcaption></figure></div>
