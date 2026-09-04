dataviz.regression.regularization.regularization_validation_plot_static
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.regularization</p></div>

.. currentmodule:: dataviz.regression.regularization

.. autofunction:: regularization_validation_plot_static

Use case
--------

Use to pick a penalty strength by comparing train and validation scores, with a fold std band when available.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.regularization import regularization_validation_plot_static

   alphas = np.logspace(-3, 2, 20)
   train_scores = 0.95 - 0.02 * np.log10(alphas + 1e-3)
   test_scores = train_scores - 0.05 - 0.01 * np.abs(np.log10(alphas))

   ax = regularization_validation_plot_static(alphas, train_scores, test_scores, score_name="R2")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/regularization/regularization_validation_plot_static.png" alt="regularization_validation_plot_static example output"><figcaption>Example output</figcaption></figure></div>
