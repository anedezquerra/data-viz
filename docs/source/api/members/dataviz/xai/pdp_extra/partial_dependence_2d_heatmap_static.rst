dataviz.xai.pdp_extra.partial_dependence_2d_heatmap_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.pdp_extra</p></div>

.. currentmodule:: dataviz.xai.pdp_extra

.. autofunction:: partial_dependence_2d_heatmap_static

Use case
--------

Use to inspect pairwise feature interactions on a precomputed 2-D partial dependence grid.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.pdp_extra import partial_dependence_2d_heatmap_static

   credit_score = np.linspace(300, 850, 25)
   dti = np.linspace(0.0, 0.6, 20)
   xx, yy = np.meshgrid(credit_score, dti)
   logit = -3.0 + 0.008 * (xx - 300) + 6.0 * yy - 0.006 * (xx - 300) * yy
   pdp = 1.0 / (1.0 + np.exp(-logit))
   ax = partial_dependence_2d_heatmap_static(
       credit_score, dti, pdp,
       feature_x="credit_score", feature_y="debt_to_income",
       title="Default risk: credit score x debt-to-income interaction",
       cmap="magma",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/pdp_extra/partial_dependence_2d_heatmap_static.png" alt="partial_dependence_2d_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
