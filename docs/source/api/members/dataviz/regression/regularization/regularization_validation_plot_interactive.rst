dataviz.regression.regularization.regularization_validation_plot_interactive
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.regularization</p></div>

.. currentmodule:: dataviz.regression.regularization

.. autofunction:: regularization_validation_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.regularization import regularization_validation_plot_interactive

   alphas = np.logspace(-3, 2, 20)
   train_scores = 0.95 - 0.02 * np.log10(alphas + 1e-3)
   test_scores = train_scores - 0.05 - 0.01 * np.abs(np.log10(alphas))

   fig = regularization_validation_plot_interactive(alphas, train_scores, test_scores, score_name="R2")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/regularization/regularization_validation_plot_interactive.png" alt="regularization_validation_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
