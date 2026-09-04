dataviz.univariate.box_plot.box_plot_static
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.box_plot</p></div>

.. currentmodule:: dataviz.univariate.box_plot

.. autofunction:: box_plot_static

Use case
--------

Use to summarize quartiles, spread, and outliers of a numeric variable, with an optional notch for median comparison.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.box_plot import box_plot_static

   # Daily household electricity consumption with a few heavy-usage days
   rng = np.random.default_rng(42)
   usage_kwh = pd.Series(
       np.concatenate([
           rng.normal(loc=18.0, scale=3.5, size=36),
           np.array([34.2, 37.8]),
       ]),
       name="usage_kwh",
   )

   ax = box_plot_static(
       usage_kwh,
       title="Daily Electricity Consumption",
       ylabel="Consumption (kWh)",
       color="lightsteelblue",
       notch=True,
       widths=0.4,
       theme="minimal",
   )
   ax.axhline(usage_kwh.mean(), color="crimson", linestyle="--", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/box_plot/box_plot_static.png" alt="box_plot_static example output"><figcaption>Example output</figcaption></figure></div>
