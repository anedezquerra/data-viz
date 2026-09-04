dataviz.bivariate.joint.bivariate_histogram_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.joint</p></div>

.. currentmodule:: dataviz.bivariate.joint

.. autofunction:: bivariate_histogram_static

Use case
--------

Use to summarize the joint distribution of two variables as rectangular bins when points overplot.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.joint import bivariate_histogram_static

   rng = np.random.default_rng(42)
   n = 600
   wait_min = pd.Series(rng.gamma(shape=3.0, scale=2.0, size=n), name="Wait time (min)")
   bill = pd.Series(15.0 + 2.0 * wait_min + rng.normal(loc=0.0, scale=8.0, size=n), name="Bill (USD)")

   ax = bivariate_histogram_static(
       wait_min,
       bill,
       bins=25,
       title="Wait Time vs Bill Density",
       cmap="rocket_r",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/joint/bivariate_histogram_static.png" alt="bivariate_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
