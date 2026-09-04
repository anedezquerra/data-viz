dataviz.regression.forecast.backtest_error_distribution_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.forecast</p></div>

.. currentmodule:: dataviz.regression.forecast

.. autofunction:: backtest_error_distribution_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.forecast import backtest_error_distribution_interactive

   rng = np.random.default_rng(42)
   errors = rng.normal(0.0, 0.7, size=120)

   fig = backtest_error_distribution_interactive(errors)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/forecast/backtest_error_distribution_interactive.png" alt="backtest_error_distribution_interactive example output"><figcaption>Example output</figcaption></figure></div>
