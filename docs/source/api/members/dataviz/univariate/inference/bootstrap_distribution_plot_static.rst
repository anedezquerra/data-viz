dataviz.univariate.inference.bootstrap_distribution_plot_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.inference</p></div>

.. currentmodule:: dataviz.univariate.inference

.. autofunction:: bootstrap_distribution_plot_static

Use case
--------

Use to visualize the bootstrap distribution of a statistic with the observed estimate marked, to judge stability and skew of the interval.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.inference import bootstrap_distribution_plot_static

   rng = np.random.default_rng(42)
   wait_minutes = pd.Series(
       rng.lognormal(mean=2.2, sigma=0.6, size=180).round(1),
       name="wait_minutes",
   )
   ax = bootstrap_distribution_plot_static(
       wait_minutes,
       statistic="mean",
       n_resamples=1000,
       seed=7,
       title="Bootstrap Mean Wait Time (Call Center)",
       color="steelblue",
   )
   ax.set_xlabel("Mean wait time (minutes)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/inference/bootstrap_distribution_plot_static.png" alt="bootstrap_distribution_plot_static example output"><figcaption>Example output</figcaption></figure></div>
