dataviz.univariate.fitting.fitted_distribution_histogram_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.fitting</p></div>

.. currentmodule:: dataviz.univariate.fitting

.. autofunction:: fitted_distribution_histogram_static

Use case
--------

Use to overlay a fitted probability density on a histogram to visually judge how well the chosen distribution fits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.fitting import fitted_distribution_histogram_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   ax = fitted_distribution_histogram_static(values, distribution="norm")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/fitting/fitted_distribution_histogram_static.png" alt="fitted_distribution_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
