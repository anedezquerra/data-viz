dataviz.regression.validation.cv_score_plot_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: cv_score_plot_interactive

Use case
--------

Use to judge model stability by inspecting per-fold cross-validation scores against their mean; high variance across folds warns of sensitivity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.validation import cv_score_plot_interactive

   rng = np.random.default_rng(42)
   fold_scores = rng.normal(0.85, 0.03, size=10)

   fig = cv_score_plot_interactive(fold_scores, model_name="Ridge")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/cv_score_plot_interactive.png" alt="cv_score_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
