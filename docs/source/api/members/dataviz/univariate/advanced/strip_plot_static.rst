dataviz.univariate.advanced.strip_plot_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: strip_plot_static

Use case
--------

Use to display each observation as a jittered point, ideal for small samples where exact values and density matter.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.advanced import strip_plot_static

   # Daily coffee-shop transaction amounts over six weeks
   rng = np.random.default_rng(42)
   amounts = pd.Series(
       np.round(rng.gamma(shape=4.0, scale=1.8, size=42), 2),
       name="transaction_usd",
   )

   ax = strip_plot_static(
       amounts,
       title="Individual Transaction Amounts",
       ylabel="Amount (USD)",
       color="darkorange",
       jitter=0.12,
       alpha=0.75,
       seed=7,
       theme="minimal",
   )
   ax.axhline(amounts.mean(), color="crimson", linestyle="--", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/strip_plot_static.png" alt="strip_plot_static example output"><figcaption>Example output</figcaption></figure></div>
