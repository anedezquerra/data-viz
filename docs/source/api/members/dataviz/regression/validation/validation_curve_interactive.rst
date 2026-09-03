dataviz.regression.validation.validation_curve_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: validation_curve_interactive

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

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
