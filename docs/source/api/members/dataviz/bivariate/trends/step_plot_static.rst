dataviz.bivariate.trends.step_plot_static
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.trends</p></div>

.. currentmodule:: dataviz.bivariate.trends

.. autofunction:: step_plot_static

Use case
--------

Use for values that change discretely at known points, such as cumulative counts or rate changes over time.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.trends import step_plot_static

   quarter = pd.Series(np.arange(1, 13), name="Quarter")
   price = pd.Series(
       [9.99, 9.99, 10.49, 10.49, 10.49, 10.99, 10.99, 11.49, 11.49, 11.49, 11.99, 11.99],
       name="Subscription price (USD)",
   )

   ax = step_plot_static(
       quarter,
       price,
       where="post",
       title="Subscription Price Changes Over Time",
       color="darkorange",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/trends/step_plot_static.png" alt="step_plot_static example output"><figcaption>Example output</figcaption></figure></div>
