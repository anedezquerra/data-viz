dataviz.univariate.treatment.outlier_treatment_comparison_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.treatment</p></div>

.. currentmodule:: dataviz.univariate.treatment

.. autofunction:: outlier_treatment_comparison_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.treatment import outlier_treatment_comparison_static

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   ax = outlier_treatment_comparison_static(values)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/univariate/treatment/outlier_treatment_comparison_static.png" alt="outlier_treatment_comparison_static example output"><figcaption>Example output</figcaption></figure></div>
