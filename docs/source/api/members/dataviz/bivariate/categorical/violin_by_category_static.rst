dataviz.bivariate.categorical.violin_by_category_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: violin_by_category_static

Use case
--------

Use when box plots hide bimodal or skewed shapes and you need the full distribution per category.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.categorical import violin_by_category_static

   rng = np.random.default_rng(42)
   n = 150
   shift = pd.Series(np.repeat(["Morning", "Afternoon", "Night"], n // 3), name="Shift")
   cycle_time = pd.Series(
       np.concatenate([
           rng.normal(loc=45.0, scale=4.0, size=n // 3),
           rng.normal(loc=52.0, scale=6.0, size=n // 3),
           rng.normal(loc=49.0, scale=3.0, size=n // 3),
       ]),
       name="Cycle time (s)",
   )

   ax = violin_by_category_static(
       shift,
       cycle_time,
       title="Cycle Time Shape by Shift",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/violin_by_category_static.png" alt="violin_by_category_static example output"><figcaption>Example output</figcaption></figure></div>
