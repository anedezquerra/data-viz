dataviz.regression.effects.ice_plot_regression_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: ice_plot_regression_static

Use case
--------

Use to reveal heterogeneous feature effects hidden by PDP: per-observation ICE lines with the average overlaid.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.effects import ice_plot_regression_static

   rng = np.random.default_rng(42)
   grid = np.linspace(0, 40, 20)
   ice = np.vstack([50 + 1.8 * grid + rng.normal(0, 8) + 0.02 * grid ** 2
                    for _ in range(15)])

   ax = ice_plot_regression_static(grid, ice,
                                   title="ICE: Commute Distance on Rent",
                                   feature_name="distance to downtown (km)",
                                   alpha=0.25)
   ax.set_ylabel("Predicted rent (USD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/ice_plot_regression_static.png" alt="ice_plot_regression_static example output"><figcaption>Example output</figcaption></figure></div>
