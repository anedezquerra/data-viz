dataviz.univariate.distribution.ecdf_plot_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: ecdf_plot_static

Use case
--------

Use to plot the empirical cumulative distribution, reading off medians and quantiles directly without binning.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.distribution import ecdf_plot_static

   # Rental durations for a bike-share station over one week
   rng = np.random.default_rng(42)
   duration_min = pd.Series(
       np.round(rng.gamma(shape=2.2, scale=9.0, size=38), 1),
       name="rental_min",
   )

   ax = ecdf_plot_static(
       duration_min,
       title="Bike-Share Rental Duration ECDF",
       xlabel="Rental Duration (min)",
       color="darkgreen",
       linewidth=2.5,
       theme="minimal",
   )
   ax.axhline(0.5, color="gray", linestyle=":", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/ecdf_plot_static.png" alt="ecdf_plot_static example output"><figcaption>Example output</figcaption></figure></div>
