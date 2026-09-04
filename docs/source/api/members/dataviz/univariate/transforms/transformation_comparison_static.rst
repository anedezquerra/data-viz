dataviz.univariate.transforms.transformation_comparison_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.transforms</p></div>

.. currentmodule:: dataviz.univariate.transforms

.. autofunction:: transformation_comparison_static

Use case
--------

Use to compare histograms of common transformations side by side when deciding how to handle skewed data.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.transforms import transformation_comparison_static

   rng = np.random.default_rng(42)
   reaction_ms = pd.Series(
       rng.gamma(shape=3.0, scale=90.0, size=150).round(1),
       name="reaction_ms",
   )
   fig = transformation_comparison_static(
       reaction_ms,
       bins=20,
       title="Reaction Time Under Common Transformations",
       color="mediumpurple",
   )
   fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/transforms/transformation_comparison_static.png" alt="transformation_comparison_static example output"><figcaption>Example output</figcaption></figure></div>
