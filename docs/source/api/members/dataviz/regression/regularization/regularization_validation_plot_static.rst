dataviz.regression.regularization.regularization_validation_plot_static
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.regularization</p></div>

.. currentmodule:: dataviz.regression.regularization

.. autofunction:: regularization_validation_plot_static

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

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
