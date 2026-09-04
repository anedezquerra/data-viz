dataviz.univariate.advanced.rug_plot_static
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: rug_plot_static

Use case
--------

Use to show every individual observation as ticks along an axis, revealing clustering and gaps that bins can hide.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.advanced import rug_plot_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   ax = rug_plot_static(values)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/rug_plot_static.png" alt="rug_plot_static example output"><figcaption>Example output</figcaption></figure></div>
