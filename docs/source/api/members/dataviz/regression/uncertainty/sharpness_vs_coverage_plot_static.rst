dataviz.regression.uncertainty.sharpness_vs_coverage_plot_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.uncertainty</p></div>

.. currentmodule:: dataviz.regression.uncertainty

.. autofunction:: sharpness_vs_coverage_plot_static

Use case
--------

Compare models on the interval-width vs coverage trade-off to find the one with the sharpest intervals that still cover the target rate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.regression.uncertainty import sharpness_vs_coverage_plot_static

   models = ["Linear+conformal", "Quantile RF", "Bayesian ridge", "NGBoost"]
   sharpness = [58.2, 44.7, 49.5, 41.3]   # average interval width (k$)
   coverage = [0.901, 0.912, 0.887, 0.928]

   ax = sharpness_vs_coverage_plot_static(
       sharpness, coverage, model_labels=models,
       title="House price intervals: sharpness vs empirical coverage",
   )
   ax.axhline(0.90, color="#e45756", linestyle=":", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/uncertainty/sharpness_vs_coverage_plot_static.png" alt="sharpness_vs_coverage_plot_static example output"><figcaption>Example output</figcaption></figure></div>
