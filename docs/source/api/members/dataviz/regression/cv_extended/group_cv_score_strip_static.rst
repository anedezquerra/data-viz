dataviz.regression.cv_extended.group_cv_score_strip_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.cv_extended</p></div>

.. currentmodule:: dataviz.regression.cv_extended

.. autofunction:: group_cv_score_strip_static

Use case
--------

Use to plot CV scores per group in grouped cross-validation, exposing groups where the model generalizes poorly.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.cv_extended import group_cv_score_strip_static

   plants = ["Plant A", "Plant B", "Plant C", "Plant D", "Plant E"]
   scores = np.array([0.72, 0.83, 0.68, 0.79, 0.75])

   ax = group_cv_score_strip_static(plants, scores,
                                    title="OEE Model: Leave-One-Plant-Out R2",
                                    metric_name="R2", color="#c0392b")
   ax.set_ylim(0.5, 1.0)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/cv_extended/group_cv_score_strip_static.png" alt="group_cv_score_strip_static example output"><figcaption>Example output</figcaption></figure></div>
