dataviz.univariate.density.density_static
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.density</p></div>

.. currentmodule:: dataviz.univariate.density

.. autofunction:: density_static

Use case
--------

Use to estimate the smooth probability density of a numeric variable without committing to histogram bins.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.density import density_static

   # Nightly server room temperatures sampled by an IoT sensor
   rng = np.random.default_rng(42)
   temp_c = pd.Series(
       np.round(rng.normal(loc=21.5, scale=1.2, size=60), 2),
       name="temperature_c",
   )

   ax = density_static(
       temp_c,
       title="Server Room Temperature Density",
       xlabel="Temperature (C)",
       color="darkred",
       linewidth=2.5,
       fill=True,
       theme="minimal",
   )
   ax.axvline(temp_c.mean(), color="navy", linestyle="--", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/density/density_static.png" alt="density_static example output"><figcaption>Example output</figcaption></figure></div>
