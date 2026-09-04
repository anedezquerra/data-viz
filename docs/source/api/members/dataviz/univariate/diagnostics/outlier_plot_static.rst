dataviz.univariate.diagnostics.outlier_plot_static
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.diagnostics</p></div>

.. currentmodule:: dataviz.univariate.diagnostics

.. autofunction:: outlier_plot_static

Use case
--------

Use an index plot that flags univariate outliers to locate which observations sit outside expected bounds.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.diagnostics import outlier_plot_static

   # Daily website sessions with two traffic spikes from a campaign
   rng = np.random.default_rng(42)
   sessions = pd.Series(
       np.concatenate([
           rng.normal(loc=4200.0, scale=380.0, size=44),
           np.array([7200.0, 2300.0]),
       ]),
       name="daily_sessions",
   )

   ax = outlier_plot_static(
       sessions,
       method="iqr",
       multiplier=1.5,
       title="Daily Session Outlier Review",
       xlabel="Day Index",
       ylabel="Sessions",
       color="steelblue",
       outlier_color="crimson",
       theme="default",
   )
   ax.set_xlabel("Day Index")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/diagnostics/outlier_plot_static.png" alt="outlier_plot_static example output"><figcaption>Example output</figcaption></figure></div>
