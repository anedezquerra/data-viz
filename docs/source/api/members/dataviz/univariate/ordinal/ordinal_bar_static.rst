dataviz.univariate.ordinal.ordinal_bar_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.ordinal</p></div>

.. currentmodule:: dataviz.univariate.ordinal

.. autofunction:: ordinal_bar_static

Use case
--------

Use to plot ordinal category counts or proportions in a fixed meaningful order, avoiding misleading frequency sorting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.ordinal import ordinal_bar_static

   rng = np.random.default_rng(42)
   scale = ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
   satisfaction = pd.Series(
       rng.choice(scale, size=220, p=[0.08, 0.17, 0.20, 0.35, 0.20]),
       name="satisfaction",
   )
   ax = ordinal_bar_static(
       satisfaction,
       order=scale,
       normalize=True,
       title="Post-Purchase Satisfaction Survey (n=220)",
       color="teal",
       theme="minimal",
   )
   ax.set_ylabel("Share of respondents")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/ordinal/ordinal_bar_static.png" alt="ordinal_bar_static example output"><figcaption>Example output</figcaption></figure></div>
