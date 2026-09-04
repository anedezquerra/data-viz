dataviz.univariate.distribution.qq_plot_static
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: qq_plot_static

Use case
--------

Use to compare sample quantiles against a theoretical distribution to assess fit, especially in the tails.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.distribution import qq_plot_static

   # Heights measured in a university anthropometry study
   rng = np.random.default_rng(42)
   height_cm = pd.Series(
       np.round(rng.normal(loc=171.0, scale=9.5, size=48), 1),
       name="height_cm",
   )

   ax = qq_plot_static(
       height_cm,
       distribution="norm",
       title="Height Normality QQ Plot",
       color="steelblue",
       reference_color="crimson",
       theme="default",
   )
   ax.set_xlabel("Theoretical Normal Quantiles")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/qq_plot_static.png" alt="qq_plot_static example output"><figcaption>Example output</figcaption></figure></div>
