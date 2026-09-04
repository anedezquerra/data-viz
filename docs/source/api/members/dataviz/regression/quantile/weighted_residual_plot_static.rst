dataviz.regression.quantile.weighted_residual_plot_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: weighted_residual_plot_static

Use case
--------

Use to check whether high-weight observations drive residual patterns in weighted or robust fits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.quantile import weighted_residual_plot_static

   rng = np.random.default_rng(42)
   towns = pd.Series(np.arange(1, 26), name="town")
   predicted_cases = pd.Series(rng.uniform(20, 220, 25).round(1), name="predicted")
   residuals = pd.Series(rng.normal(0, 14, 25).round(2), name="residual")
   sample_size = pd.Series(rng.integers(120, 4000, 25), name="survey_n")
   weights = sample_size / sample_size.max()

   ax = weighted_residual_plot_static(
       predicted_cases, residuals, weights,
       title="Epidemiology survey: residuals weighted by sample size",
       cmap="plasma", theme="minimal",
   )
   ax.set_xlabel("Predicted weekly cases")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/quantile/weighted_residual_plot_static.png" alt="weighted_residual_plot_static example output"><figcaption>Example output</figcaption></figure></div>
