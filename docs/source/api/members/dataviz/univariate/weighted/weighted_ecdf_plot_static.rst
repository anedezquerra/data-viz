dataviz.univariate.weighted.weighted_ecdf_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.weighted</p></div>

.. currentmodule:: dataviz.univariate.weighted

.. autofunction:: weighted_ecdf_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.weighted import weighted_ecdf_plot_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")
   weights = pd.Series([1.0, 1.5, 0.8, 1.2, 1.0, 1.1], name="Weight")

   ax = weighted_ecdf_plot_static(values, weights)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/weighted/weighted_ecdf_plot_static.png" alt="weighted_ecdf_plot_static example output"><figcaption>Example output</figcaption></figure></div>
