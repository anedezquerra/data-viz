dataviz.classification.calibration_extra.score_qq_by_class_static
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: score_qq_by_class_static

Use case
--------

Use to spot distributional skew in scores per class by plotting class quantiles against a uniform reference.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.calibration_extra import score_qq_by_class_static

   rng = np.random.default_rng(17)
   n_pos, n_neg = 50, 100
   y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
   y_score = np.concatenate([
       rng.beta(5, 3, n_pos),
       rng.beta(3, 5, n_neg),
   ]).clip(0.01, 0.99)

   ax = score_qq_by_class_static(
       y_true, y_score, labels=[0, 1], n_quantiles=30,
       title="Credit approval model: score Q-Q vs uniform by class",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration_extra/score_qq_by_class_static.png" alt="score_qq_by_class_static example output"><figcaption>Example output</figcaption></figure></div>
