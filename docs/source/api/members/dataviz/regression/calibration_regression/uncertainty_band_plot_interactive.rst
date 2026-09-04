dataviz.regression.calibration_regression.uncertainty_band_plot_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.calibration_regression</p></div>

.. currentmodule:: dataviz.regression.calibration_regression

.. autofunction:: uncertainty_band_plot_interactive

Use case
--------

Use to visualize predictive mean with a plus/minus z-sigma band, e.g. for Gaussian process regression, to see where the model is uncertain.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.calibration_regression import uncertainty_band_plot_interactive

   rng = np.random.default_rng(42)
   n = 30
   mean_pred = pd.Series(np.sort(rng.uniform(200, 800, n)), name="gp_mean_cycles")
   sigma = pd.Series(rng.uniform(20, 60, n), name="gp_std_cycles")
   observed = pd.Series(mean_pred + rng.normal(0, 1, n) * sigma,
                        name="observed_cycles")

   fig = uncertainty_band_plot_interactive(
       observed, mean_pred, sigma, z=1.96,
       title="Battery Life GP Model: Predictive Uncertainty Band",
       line_color="#c0392b", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/calibration_regression/uncertainty_band_plot_interactive.png" alt="uncertainty_band_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
