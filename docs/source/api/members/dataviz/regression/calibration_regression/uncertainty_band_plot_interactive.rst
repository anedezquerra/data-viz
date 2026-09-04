dataviz.regression.calibration_regression.uncertainty_band_plot_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.calibration_regression</p></div>

.. currentmodule:: dataviz.regression.calibration_regression

.. autofunction:: uncertainty_band_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.calibration_regression import uncertainty_band_plot_interactive

   rng = np.random.default_rng(42)
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)
   y_std = np.full(60, 0.6)

   fig = uncertainty_band_plot_interactive(y_true, y_pred, y_std)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/calibration_regression/uncertainty_band_plot_interactive.png" alt="uncertainty_band_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
