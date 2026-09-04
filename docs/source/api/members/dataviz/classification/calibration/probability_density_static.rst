dataviz.classification.calibration.probability_density_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration</p></div>

.. currentmodule:: dataviz.classification.calibration

.. autofunction:: probability_density_static

Use case
--------

Use for a smooth per-class view of predicted probability density when histograms are too coarse or noisy.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.calibration import probability_density_static

   rng = np.random.default_rng(11)
   n_pos, n_neg = 50, 100
   y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
   y_prob = np.concatenate([
       np.clip(rng.beta(6, 2, n_pos), 0.01, 0.99),
       np.clip(rng.beta(2, 6, n_neg), 0.01, 0.99),
   ])

   ax = probability_density_static(
       y_true, y_prob, bandwidth=0.08,
       title="Diabetes screening test: probability density by outcome",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration/probability_density_static.png" alt="probability_density_static example output"><figcaption>Example output</figcaption></figure></div>
