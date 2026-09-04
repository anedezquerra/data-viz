dataviz.univariate.advanced.lollipop_chart_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: lollipop_chart_static

Use case
--------

Use to compare category counts with stems and markers when bars feel too heavy for a slim ranking view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.advanced import lollipop_chart_static

   # Online orders grouped by product category for one month
   rng = np.random.default_rng(42)
   categories = pd.Series(
       rng.choice(
           ["Books", "Electronics", "Clothing", "Home", "Toys", "Sports", "Beauty"],
           size=280,
           p=[0.24, 0.22, 0.18, 0.14, 0.10, 0.07, 0.05],
       ),
       name="category",
   )

   ax = lollipop_chart_static(
       categories,
       title="Monthly Orders by Product Category",
       xlabel="Product Category",
       ylabel="Orders",
       color="navy",
       stem_color="lightgray",
       top_n=7,
       theme="minimal",
   )
   ax.set_ylabel("Orders")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/lollipop_chart_static.png" alt="lollipop_chart_static example output"><figcaption>Example output</figcaption></figure></div>
