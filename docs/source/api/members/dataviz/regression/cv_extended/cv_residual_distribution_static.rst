dataviz.regression.cv_extended.cv_residual_distribution_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.cv_extended</p></div>

.. currentmodule:: dataviz.regression.cv_extended

.. autofunction:: cv_residual_distribution_static

Use case
--------

Use to compare residual boxplots across CV folds and check that errors are stable rather than driven by one lucky or unlucky split.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.cv_extended import cv_residual_distribution_static

   rng = np.random.default_rng(42)
   fold_labels = ["Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5"]
   residuals_per_fold = [rng.normal(0.0, 0.5 + 0.1 * i, size=20) for i in range(5)]

   ax = cv_residual_distribution_static(fold_labels, residuals_per_fold)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/cv_extended/cv_residual_distribution_static.png" alt="cv_residual_distribution_static example output"><figcaption>Example output</figcaption></figure></div>
