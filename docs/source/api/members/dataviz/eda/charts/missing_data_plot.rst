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
   import matplotlib.pyplot as plt
   from dataviz.eda.charts import missing_data_plot

   rng = np.random.default_rng(42)
   n = 100
   df = pd.DataFrame({
       "Customer ID": np.arange(1, n + 1),
       "Age": rng.integers(18, 75, size=n).astype(float),
       "Income": rng.normal(loc=60000.0, scale=15000.0, size=n),
       "Email": rng.choice(["user@example.com", None], size=n, p=[0.8, 0.2]),
       "Last purchase": rng.choice(["2024-05-01", None], size=n, p=[0.9, 0.1]),
   })
   df.loc[rng.choice(n, size=12, replace=False), "Age"] = np.nan
   df.loc[rng.choice(n, size=8, replace=False), "Income"] = np.nan

   ax = missing_data_plot(df, title="CRM Export Missing Data Profile")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/eda/charts/missing_data_plot.png" alt="missing_data_plot example output"><figcaption>Example output</figcaption></figure></div>
