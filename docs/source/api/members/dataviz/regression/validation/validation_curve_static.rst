dataviz.regression.validation.validation_curve_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: validation_curve_static

Use case
--------

Use to tune a hyperparameter by plotting train and validation scores against its values; widening gaps signal overfitting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.validation import validation_curve_static

   rng = np.random.default_rng(42)
   alphas = np.logspace(-3, 2, 12)
   base_train = 0.55 + 0.40 * (1 - np.exp(-alphas))
   base_test = 0.88 - 0.0011 * (np.log10(alphas) + 1.2) ** 4
   train_scores = base_train[:, None] + rng.normal(0, 0.012, (12, 5))
   test_scores = base_test[:, None] + rng.normal(0, 0.020, (12, 5))

   ax = validation_curve_static(
       alphas, train_scores, test_scores,
       param_name="Ridge alpha", score_name="R-squared", log_x=True,
       title="Ridge regression on concrete strength: validation curve",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/validation_curve_static.png" alt="validation_curve_static example output"><figcaption>Example output</figcaption></figure></div>
