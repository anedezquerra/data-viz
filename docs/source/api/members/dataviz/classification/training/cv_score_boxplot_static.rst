dataviz.classification.training.cv_score_boxplot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.training</p></div>

.. currentmodule:: dataviz.classification.training

.. autofunction:: cv_score_boxplot_static

Use case
--------

Use to compare model candidates on cross-validation stability; one box per model over per-fold scores.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.training import cv_score_boxplot_static

   rng = np.random.default_rng(42)
   # 10-fold CV F1 scores for four churn model candidates
   cv_scores = {
       "logreg": rng.normal(0.72, 0.03, 10),
       "random forest": rng.normal(0.79, 0.025, 10),
       "gradient boost": rng.normal(0.81, 0.02, 10),
       "naive bayes": rng.normal(0.66, 0.04, 10),
   }

   ax = cv_score_boxplot_static(cv_scores,
                                title="Churn models: 10-fold CV F1")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/training/cv_score_boxplot_static.png" alt="cv_score_boxplot_static example output"><figcaption>Example output</figcaption></figure></div>
