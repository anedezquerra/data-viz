dataviz.eda.charts.missing_data_plot
====================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.eda.charts</p></div>

.. currentmodule:: dataviz.eda.charts

.. autofunction:: missing_data_plot

Use case
--------

Use when auditing a dataset for missing values before modeling to see which columns need imputation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.eda.charts import missing_data_plot

   df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [4, 3, 2, 1], "segment": ["A", "A", "B", "B"]})

   result = missing_data_plot(df)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/eda/charts/missing_data_plot.png" alt="missing_data_plot example output"><figcaption>Example output</figcaption></figure></div>
