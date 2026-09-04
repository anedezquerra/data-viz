dataviz.classification.training.validation_curve_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.training</p></div>

.. currentmodule:: dataviz.classification.training

.. autofunction:: validation_curve_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.training import validation_curve_interactive

   param_values = np.array([0.001, 0.01, 0.1, 1.0, 10.0, 100.0])
   train_scores = np.array([0.78, 0.82, 0.88, 0.93, 0.97, 0.99])
   val_scores = np.array([0.77, 0.81, 0.86, 0.87, 0.84, 0.80])

   fig = validation_curve_interactive(param_values, train_scores, val_scores, param_name="C")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/training/validation_curve_interactive.png" alt="validation_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
