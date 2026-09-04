dataviz.bivariate.advanced.hexbin_plot_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: hexbin_plot_static

Use case
--------

Use when a scatter plot of a large dataset overplots, to see point density as hexagonal bins.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.advanced import hexbin_plot_static

   rng = np.random.default_rng(42)
   n = 2000
   load = pd.Series(rng.normal(loc=70.0, scale=8.0, size=n), name="Server load (%)")
   latency = pd.Series(20.0 + 0.8 * load + rng.normal(loc=0.0, scale=6.0, size=n), name="Latency (ms)")

   ax = hexbin_plot_static(
       load,
       latency,
       gridsize=25,
       title="Latency vs Server Load Density",
       cmap="magma",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/hexbin_plot_static.png" alt="hexbin_plot_static example output"><figcaption>Example output</figcaption></figure></div>
