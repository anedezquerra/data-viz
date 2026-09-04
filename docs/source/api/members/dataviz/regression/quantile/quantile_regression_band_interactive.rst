dataviz.regression.quantile.quantile_regression_band_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: quantile_regression_band_interactive

Use case
--------

Use to visualize fitted low/median/high quantile curves against the data when modeling more than the conditional mean.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.quantile import quantile_regression_band_interactive

   rng = np.random.default_rng(42)
   x = np.linspace(0.0, 10.0, 60)
   y = 2 * x + rng.normal(0.0, 1.0, size=60)
   y_low = 2 * x - 1.5
   y_med = 2 * x
   y_high = 2 * x + 1.5

   fig = quantile_regression_band_interactive(x, y, y_low, y_med, y_high)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/quantile/quantile_regression_band_interactive.png" alt="quantile_regression_band_interactive example output"><figcaption>Example output</figcaption></figure></div>
