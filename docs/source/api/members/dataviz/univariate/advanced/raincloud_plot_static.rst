dataviz.univariate.advanced.raincloud_plot_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: raincloud_plot_static

Use case
--------

Use to combine density, box plot, and raw points in one raincloud view showing shape, quartiles, and observations together.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.advanced import raincloud_plot_static

   # Resting heart rates recorded by a wellness study cohort
   rng = np.random.default_rng(42)
   heart_rate = pd.Series(
       np.round(rng.normal(loc=68.0, scale=7.5, size=55), 1),
       name="heart_rate_bpm",
   )

   ax = raincloud_plot_static(
       heart_rate,
       title="Resting Heart Rate Raincloud",
       ylabel="Heart Rate (bpm)",
       color="mediumpurple",
       alpha=0.55,
       theme="minimal",
   )
   ax.set_ylabel("Heart Rate (bpm)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/raincloud_plot_static.png" alt="raincloud_plot_static example output"><figcaption>Example output</figcaption></figure></div>
