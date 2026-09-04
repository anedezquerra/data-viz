dataviz.univariate.diagnostics.percentile_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.diagnostics</p></div>

.. currentmodule:: dataviz.univariate.diagnostics

.. autofunction:: percentile_plot_static

Use case
--------

Use to profile a variable across its percentiles, revealing tail behavior and skew beyond mean and standard deviation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.diagnostics import percentile_plot_static

   # Response times for an internal API endpoint over one day
   rng = np.random.default_rng(42)
   response_ms = pd.Series(
       np.round(rng.lognormal(mean=4.6, sigma=0.5, size=58), 1),
       name="response_ms",
   )

   ax = percentile_plot_static(
       response_ms,
       step=10,
       title="API Response Time Percentile Profile",
       xlabel="Percentile",
       ylabel="Response Time (ms)",
       color="darkmagenta",
       marker="s",
       theme="minimal",
   )
   ax.set_ylabel("Response Time (ms)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/diagnostics/percentile_plot_static.png" alt="percentile_plot_static example output"><figcaption>Example output</figcaption></figure></div>
