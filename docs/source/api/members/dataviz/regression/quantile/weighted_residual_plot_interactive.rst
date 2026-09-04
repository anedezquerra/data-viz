dataviz.regression.quantile.weighted_residual_plot_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: weighted_residual_plot_interactive

Use case
--------

Use to check whether high-weight observations drive residual patterns in weighted or robust fits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.quantile import weighted_residual_plot_interactive

   rng = np.random.default_rng(42)
   y_pred = rng.normal(10.0, 2.0, size=60)
   residuals = rng.normal(0.0, 0.7, size=60)
   weights = rng.uniform(0.5, 1.5, size=60)

   fig = weighted_residual_plot_interactive(y_pred, residuals, weights)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/quantile/weighted_residual_plot_interactive.png" alt="weighted_residual_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
