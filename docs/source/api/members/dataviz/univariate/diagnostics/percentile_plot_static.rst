dataviz.univariate.diagnostics.percentile_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.diagnostics</p></div>

.. currentmodule:: dataviz.univariate.diagnostics

.. autofunction:: percentile_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.diagnostics import percentile_plot_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   ax = percentile_plot_static(values)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/diagnostics/percentile_plot_static.png" alt="percentile_plot_static example output"><figcaption>Example output</figcaption></figure></div>
