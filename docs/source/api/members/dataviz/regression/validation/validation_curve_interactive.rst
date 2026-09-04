dataviz.regression.validation.validation_curve_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: validation_curve_interactive

Use case
--------

Use to tune a hyperparameter by plotting train and validation scores against its values; widening gaps signal overfitting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.validation import validation_curve_interactive

   rng = np.random.default_rng(42)
   param_values = np.arange(1, 11)
   train_scores = np.clip(
       0.90 + 0.01 * param_values[:, None] + rng.normal(0.0, 0.01, size=(10, 5)), 0, 1
   )
   test_scores = np.clip(
       0.75 + 0.015 * param_values[:, None] - 0.002 * param_values[:, None] ** 2
       + rng.normal(0.0, 0.015, size=(10, 5)),
       0, 1,
   )

   fig = validation_curve_interactive(param_values, train_scores, test_scores, param_name="depth")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/validation_curve_interactive.png" alt="validation_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
