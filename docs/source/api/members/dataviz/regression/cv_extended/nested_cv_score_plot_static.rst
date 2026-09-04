dataviz.regression.cv_extended.nested_cv_score_plot_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.cv_extended</p></div>

.. currentmodule:: dataviz.regression.cv_extended

.. autofunction:: nested_cv_score_plot_static

Use case
--------

Use to display outer-fold scores from nested CV, giving an unbiased estimate of performance after hyperparameter tuning.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.cv_extended import nested_cv_score_plot_static

   outer_folds = ["Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5"]
   scores = np.array([0.81, 0.77, 0.84, 0.79, 0.82])

   ax = nested_cv_score_plot_static(outer_folds, scores,
                                    title="Churn Value Model: Nested CV R2",
                                    metric_name="R2", color="#2a7f62")
   ax.set_ylim(0.6, 0.9)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/cv_extended/nested_cv_score_plot_static.png" alt="nested_cv_score_plot_static example output"><figcaption>Example output</figcaption></figure></div>
