dataviz.bivariate.categorical.grouped_bar_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: grouped_bar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.categorical import grouped_bar_static

   rng = np.random.default_rng(42)
   category = pd.Series(np.repeat(["Line A", "Line B", "Line C"], 10), name="Line")
   values = pd.Series(rng.normal(loc=10.0, scale=1.0, size=30), name="Output")

   ax = grouped_bar_static(category, values, title="Mean output by line")
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/bivariate/categorical/grouped_bar_static.png" alt="grouped_bar_static example output"><figcaption>Example output</figcaption></figure></div>
