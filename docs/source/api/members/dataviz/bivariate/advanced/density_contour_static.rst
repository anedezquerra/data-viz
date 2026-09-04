dataviz.bivariate.advanced.density_contour_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: density_contour_static

Use case
--------

Use to visualize the joint density of two variables as contour lines when individual points are too dense to read.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.advanced import density_contour_static

   rng = np.random.default_rng(42)
   n = 800
   temperature = pd.Series(rng.normal(loc=22.0, scale=3.0, size=n), name="Temperature (C)")
   humidity = pd.Series(80.0 - 1.5 * temperature + rng.normal(loc=0.0, scale=5.0, size=n), name="Humidity (%)")

   ax = density_contour_static(
       temperature,
       humidity,
       bins=25,
       levels=10,
       title="Greenhouse Climate Density",
       cmap="cividis",
       fill=True,
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/density_contour_static.png" alt="density_contour_static example output"><figcaption>Example output</figcaption></figure></div>
