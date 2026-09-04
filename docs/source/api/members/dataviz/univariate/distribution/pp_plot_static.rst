dataviz.univariate.distribution.pp_plot_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: pp_plot_static

Use case
--------

Use to compare cumulative probabilities between data and a theoretical distribution to check fit near the center.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.distribution import pp_plot_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   ax = pp_plot_static(values)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/pp_plot_static.png" alt="pp_plot_static example output"><figcaption>Example output</figcaption></figure></div>
