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
   folds = ["Fold 1", "Fold 2", "Fold 3", "Fold 4"]
   residuals = [rng.normal(0, 4, 15),
                rng.normal(1.5, 5, 15),
                rng.normal(-0.8, 3.5, 15),
                rng.normal(0.4, 6, 15)]

   ax = cv_residual_distribution_static(
       folds, residuals,
       title="Concrete Strength Model: Residuals per CV Fold",
       color="#1f6fb2")
   ax.set_ylabel("Residual (MPa)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/cv_extended/cv_residual_distribution_static.png" alt="cv_residual_distribution_static example output"><figcaption>Example output</figcaption></figure></div>
