dataviz.classification.model_comparison.critical_difference_diagram_static
==========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: critical_difference_diagram_static

Use case
--------

Use to compare classifiers across multiple datasets via average ranks and a critical-difference threshold.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.model_comparison import (
       critical_difference_diagram_static,
   )

   rng = np.random.default_rng(73)
   # ranks of 4 models on 12 benchmark datasets (1 = best)
   rank_table = {
       "gbm": np.clip(rng.normal(1.8, 0.6, 12), 1, 4),
       "random forest": np.clip(rng.normal(2.2, 0.7, 12), 1, 4),
       "logreg": np.clip(rng.normal(3.0, 0.6, 12), 1, 4),
       "knn": np.clip(rng.normal(3.4, 0.5, 12), 1, 4),
   }

   ax = critical_difference_diagram_static(
       rank_table, cd=1.15,
       title="CD diagram: tabular benchmarks (Nemenyi, alpha=0.05)",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/critical_difference_diagram_static.png" alt="critical_difference_diagram_static example output"><figcaption>Example output</figcaption></figure></div>
