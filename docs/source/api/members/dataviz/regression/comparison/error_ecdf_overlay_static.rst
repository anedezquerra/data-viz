dataviz.regression.comparison.error_ecdf_overlay_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: error_ecdf_overlay_static

Use case
--------

Compare empirical CDFs of absolute error per model; the curve farthest up and left dominates on typical error magnitude.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.comparison import error_ecdf_overlay_static

   rng = np.random.default_rng(42)
   errors = [rng.normal(0, 4, 35),
             rng.normal(0, 7, 35),
             rng.normal(2, 10, 35)]
   labels = ["OLS", "Huber", "Quantile (median)"]

   ax = error_ecdf_overlay_static(errors, labels,
                                  title="Delivery-Time Models: |Error| ECDF",
                                  cmap="plasma")
   ax.set_xlabel("Absolute error (minutes)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/error_ecdf_overlay_static.png" alt="error_ecdf_overlay_static example output"><figcaption>Example output</figcaption></figure></div>
