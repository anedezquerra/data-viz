dataviz.regression.autocorrelation.residual_runs_plot_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.autocorrelation</p></div>

.. currentmodule:: dataviz.regression.autocorrelation

.. autofunction:: residual_runs_plot_static

Use case
--------

Use to spot non-random runs of positive or negative residuals, a quick check for structure the model failed to capture.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.autocorrelation import residual_runs_plot_static

   rng = np.random.default_rng(42)
   run = np.arange(28)
   strength = pd.Series(32 + 0.15 * run + rng.normal(0, 0.9, 28),
                        name="tensile_strength_mpa")
   fitted = pd.Series(np.full(28, 32.0 + 0.15 * 13.5), name="mean_only_fit")

   ax = residual_runs_plot_static(strength, fitted,
                                  title="Tensile Strength: Residual Runs Chart",
                                  positive_color="#2a7f62",
                                  negative_color="#c0392b")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/autocorrelation/residual_runs_plot_static.png" alt="residual_runs_plot_static example output"><figcaption>Example output</figcaption></figure></div>
