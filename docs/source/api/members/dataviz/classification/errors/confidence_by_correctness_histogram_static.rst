dataviz.classification.errors.confidence_by_correctness_histogram_static
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.errors</p></div>

.. currentmodule:: dataviz.classification.errors

.. autofunction:: confidence_by_correctness_histogram_static

Use case
--------

Use to check whether the model is confident when right and uncertain when wrong; overlapping tails flag overconfidence.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.errors import (
       confidence_by_correctness_histogram_static,
   )

   rng = np.random.default_rng(31)
   n = 150
   skill = rng.normal(0, 1.4, n)
   y_prob = 1.0 / (1.0 + np.exp(-skill))
   y_true = (skill + rng.normal(0, 1.0, n) > 0).astype(int)

   ax = confidence_by_correctness_histogram_static(
       y_true, y_prob, threshold=0.5, bins=25,
       title="Email spam filter: is the model confident when wrong?",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/errors/confidence_by_correctness_histogram_static.png" alt="confidence_by_correctness_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
