dataviz.classification.calibration.brier_score_bar_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration</p></div>

.. currentmodule:: dataviz.classification.calibration

.. autofunction:: brier_score_bar_static

Use case
--------

Compare models or classes on Brier score to rank probability quality; lower bars are better.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.classification.calibration import brier_score_bar_static

   scores = {
       "Logistic regression": 0.142,
       "Random forest": 0.118,
       "Gradient boosting": 0.105,
       "Naive base rate": 0.210,
   }

   ax = brier_score_bar_static(
       scores, title="Churn models: Brier score on Q4 holdout",
   )
   ax.set_ylim(0, 0.25)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration/brier_score_bar_static.png" alt="brier_score_bar_static example output"><figcaption>Example output</figcaption></figure></div>
