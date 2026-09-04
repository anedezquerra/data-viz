dataviz.regression.forecast.backtest_error_distribution_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: backtest_error_distribution_static

Use case
--------

Use to inspect the distribution of backtest errors for bias, skew, and heavy tails.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.forecast import backtest_error_distribution_static

   rng = np.random.default_rng(42)
   errors = rng.normal(0.0, 0.7, size=120)

   ax = backtest_error_distribution_static(errors)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/forecast/backtest_error_distribution_static.png" alt="backtest_error_distribution_static example output"><figcaption>Example output</figcaption></figure></div>
