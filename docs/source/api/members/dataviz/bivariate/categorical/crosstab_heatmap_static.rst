dataviz.bivariate.categorical.crosstab_heatmap_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: crosstab_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.categorical import crosstab_heatmap_static

   rng = np.random.default_rng(42)
   row_category = pd.Series(rng.choice(["Line A", "Line B", "Line C"], size=60), name="Line")
   column_category = pd.Series(rng.choice(["Pass", "Fail"], size=60), name="Result")

   ax = crosstab_heatmap_static(row_category, column_category, normalize="index")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/crosstab_heatmap_static.png" alt="crosstab_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
