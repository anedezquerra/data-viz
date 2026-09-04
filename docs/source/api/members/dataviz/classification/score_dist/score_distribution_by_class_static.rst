dataviz.classification.score_dist.score_distribution_by_class_static
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.score_dist</p></div>

.. currentmodule:: dataviz.classification.score_dist

.. autofunction:: score_distribution_by_class_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.score_dist import score_distribution_by_class_static

   rng = np.random.default_rng(42)
   y_score = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_score)

   ax = score_distribution_by_class_static(y_true, y_score)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/score_dist/score_distribution_by_class_static.png" alt="score_distribution_by_class_static example output"><figcaption>Example output</figcaption></figure></div>
