dataviz.classification.model_comparison.psi_bar_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: psi_bar_static

Use case
--------

Use to quantify population stability with per-bin PSI contributions and the total PSI against stability tiers.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.model_comparison import psi_bar_static

   rng = np.random.default_rng(83)
   scores_reference = np.clip(rng.beta(2, 4, 150), 0.01, 0.99)
   # seasonal campaign pushed noticeably higher-risk applicants into the funnel
   scores_current = np.clip(rng.beta(3.0, 3.4, 150), 0.01, 0.99)

   ax = psi_bar_static(
       scores_reference, scores_current, n_bins=8,
       title="Application risk score: PSI vs training baseline",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/psi_bar_static.png" alt="psi_bar_static example output"><figcaption>Example output</figcaption></figure></div>
