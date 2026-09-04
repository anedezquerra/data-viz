dataviz.classification.calibration_extra.score_ecdf_by_class_interactive
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: score_ecdf_by_class_interactive

Use case
--------

Use to compare full score distributions per class without binning; separated ECDFs signal good ranking power.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.calibration_extra import score_ecdf_by_class_interactive

   rng = np.random.default_rng(42)
   y_score = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_score)

   fig = score_ecdf_by_class_interactive(y_true, y_score)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration_extra/score_ecdf_by_class_interactive.png" alt="score_ecdf_by_class_interactive example output"><figcaption>Example output</figcaption></figure></div>
