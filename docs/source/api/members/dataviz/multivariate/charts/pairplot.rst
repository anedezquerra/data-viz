dataviz.multivariate.charts.pairplot
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.charts</p></div>

.. currentmodule:: dataviz.multivariate.charts

.. autofunction:: pairplot

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.multivariate.charts import pairplot

   df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [4, 3, 2, 1], "segment": ["A", "A", "B", "B"]})

   result = pairplot(df)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/multivariate/charts/pairplot.png" alt="pairplot example output"><figcaption>Example output</figcaption></figure></div>
