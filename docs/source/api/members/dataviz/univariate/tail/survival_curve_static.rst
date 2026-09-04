dataviz.univariate.tail.survival_curve_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.tail</p></div>

.. currentmodule:: dataviz.univariate.tail

.. autofunction:: survival_curve_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.tail import survival_curve_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   ax = survival_curve_static(values)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/tail/survival_curve_static.png" alt="survival_curve_static example output"><figcaption>Example output</figcaption></figure></div>
