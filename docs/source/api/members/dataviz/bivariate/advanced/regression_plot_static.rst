dataviz.bivariate.advanced.regression_plot_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.advanced</p></div>

.. currentmodule:: dataviz.bivariate.advanced

.. autofunction:: regression_plot_static

Use case
--------

Use to overlay a polynomial trend line on a scatter plot when assessing whether a simple curve fits the relationship.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.bivariate.advanced import regression_plot_static

   rng = np.random.default_rng(42)
   n = 50
   spend = pd.Series(rng.uniform(low=5.0, high=100.0, size=n), name="Marketing spend (k USD)")
   revenue = pd.Series(
       50.0 + 3.2 * spend - 0.015 * spend**2 + rng.normal(loc=0.0, scale=18.0, size=n),
       name="Revenue (k USD)",
   )

   ax = regression_plot_static(
       spend,
       revenue,
       degree=2,
       title="Revenue Response to Marketing Spend",
       scatter_color="darkslategray",
       line_color="crimson",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/advanced/regression_plot_static.png" alt="regression_plot_static example output"><figcaption>Example output</figcaption></figure></div>
