dataviz.bivariate.stats.conditional_box_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: conditional_box_static

Use case
--------

Use to see how the full distribution of y changes as a numeric conditioning variable x increases across bins.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.stats import conditional_box_static

   rng = np.random.default_rng(42)
   n = 180
   temperature = pd.Series(rng.uniform(low=150.0, high=250.0, size=n), name="Oven temperature (C)")
   hardness = pd.Series(30.0 + 0.25 * temperature + rng.normal(loc=0.0, scale=4.0, size=n), name="Coating hardness")

   ax = conditional_box_static(
       temperature,
       hardness,
       bins=6,
       title="Hardness Distribution by Temperature Band",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/conditional_box_static.png" alt="conditional_box_static example output"><figcaption>Example output</figcaption></figure></div>
