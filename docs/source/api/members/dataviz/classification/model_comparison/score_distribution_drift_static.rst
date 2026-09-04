dataviz.classification.model_comparison.score_distribution_drift_static
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: score_distribution_drift_static

Use case
--------

Use to monitor production models by overlaying reference vs. current score distributions for drift.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.model_comparison import (
       score_distribution_drift_static,
   )

   rng = np.random.default_rng(79)
   scores_reference = np.clip(rng.beta(2, 4, 150), 0.01, 0.99)
   # production traffic shifted toward higher risk scores last month
   scores_current = np.clip(rng.beta(2.6, 3.6, 150), 0.01, 0.99)

   ax = score_distribution_drift_static(
       scores_reference, scores_current, bins=30,
       title="Fraud scoring service: training vs last-month traffic",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/score_distribution_drift_static.png" alt="score_distribution_drift_static example output"><figcaption>Example output</figcaption></figure></div>
