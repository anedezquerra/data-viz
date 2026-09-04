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

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.density import density_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   ax = density_static(values)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/density/density_static.png" alt="density_static example output"><figcaption>Example output</figcaption></figure></div>
