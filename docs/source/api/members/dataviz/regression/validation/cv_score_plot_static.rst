dataviz.regression.validation.cv_score_plot_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: cv_score_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.validation import cv_score_plot_static

   rng = np.random.default_rng(42)
   fold_scores = rng.normal(0.85, 0.03, size=10)

   ax = cv_score_plot_static(fold_scores, model_name="Ridge")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/cv_score_plot_static.png" alt="cv_score_plot_static example output"><figcaption>Example output</figcaption></figure></div>
