dataviz.univariate.histogram.histogram_static
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.histogram</p></div>

.. currentmodule:: dataviz.univariate.histogram

.. autofunction:: histogram_static

Use case
--------

Use when profiling a numeric column for the first time to see shape, spread, and outliers at a glance.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.histogram import histogram_static

   # Call-center wait times sampled during business hours
   rng = np.random.default_rng(42)
   wait_min = pd.Series(
       np.round(rng.gamma(shape=2.0, scale=2.5, size=60), 1),
       name="wait_time_min",
   )

   ax = histogram_static(
       wait_min,
       bins=14,
       title="Call-Center Wait Time Distribution",
       xlabel="Wait Time (min)",
       ylabel="Calls",
       color="cornflowerblue",
       edgecolor="black",
       alpha=0.8,
       theme="minimal",
   )
   ax.axvline(wait_min.mean(), color="crimson", linestyle="--", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/histogram/histogram_static.png" alt="histogram_static example output"><figcaption>Example output</figcaption></figure></div>
