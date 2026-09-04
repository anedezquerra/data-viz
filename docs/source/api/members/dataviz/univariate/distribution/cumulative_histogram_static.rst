dataviz.univariate.distribution.cumulative_histogram_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: cumulative_histogram_static

Use case
--------

Use to show cumulative counts across bins when the running total of observations matters more than per-bin frequency.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.distribution import cumulative_histogram_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   ax = cumulative_histogram_static(values)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/cumulative_histogram_static.png" alt="cumulative_histogram_static example output"><figcaption>Example output</figcaption></figure></div>
