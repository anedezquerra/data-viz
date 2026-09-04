dataviz.regression.bayesian.trace_plot_coefficients_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.bayesian</p></div>

.. currentmodule:: dataviz.regression.bayesian

.. autofunction:: trace_plot_coefficients_static

Use case
--------

Use to diagnose MCMC sampling health, checking chains for good mixing and stationarity before trusting posterior summaries.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.bayesian import trace_plot_coefficients_static

   rng = np.random.default_rng(42)
   iters = np.arange(500)
   traces = [1.8 * (1 - np.exp(-iters / 80)) + rng.normal(0, 0.15, 500),
             -0.6 * (1 - np.exp(-iters / 60)) + rng.normal(0, 0.1, 500),
             rng.normal(0.9, 0.2, 500)]
   names = ["intercept", "dose_mg", "age_years"]

   ax = trace_plot_coefficients_static(traces, coef_names=names,
                                       title="MCMC Traces: Dose-Response Model",
                                       cmap="Dark2")
   ax.set_xlabel("Iteration")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/bayesian/trace_plot_coefficients_static.png" alt="trace_plot_coefficients_static example output"><figcaption>Example output</figcaption></figure></div>
