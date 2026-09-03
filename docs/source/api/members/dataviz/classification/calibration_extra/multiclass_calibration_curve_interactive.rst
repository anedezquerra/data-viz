dataviz.classification.calibration_extra.multiclass_calibration_curve_interactive
=================================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: multiclass_calibration_curve_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.calibration_extra import multiclass_calibration_curve_interactive

   rng = np.random.default_rng(42)
   logits = rng.normal(size=(200, 3))
   exp_logits = np.exp(logits - logits.max(axis=1, keepdims=True))
   y_prob_matrix = exp_logits / exp_logits.sum(axis=1, keepdims=True)
   y_true = rng.choice(3, size=200, p=[0.4, 0.35, 0.25])

   fig = multiclass_calibration_curve_interactive(y_true, y_prob_matrix, labels=["A", "B", "C"])
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
