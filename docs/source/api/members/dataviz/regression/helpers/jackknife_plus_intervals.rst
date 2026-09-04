dataviz.regression.helpers.jackknife_plus_intervals
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autofunction:: jackknife_plus_intervals

Use case
--------

Use to build Jackknife+ prediction intervals when you need coverage guarantees without distribution assumptions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.helpers import jackknife_plus_intervals

   rng = np.random.default_rng(42)
   n_cal, n_test = 25, 6
   y_calibration = pd.Series(rng.normal(70.0, 8.0, n_cal), name="yield_kg")
   loo_predictions = (y_calibration.to_numpy()[:, None]
                      + rng.normal(0.0, 1.5, (n_cal, n_test)))
   new_predictions = pd.Series(rng.normal(70.0, 2.0, n_test), name="plot_forecast")
   lower, upper = jackknife_plus_intervals(loo_predictions, y_calibration,
                                           new_predictions, alpha=0.1)
   print(pd.DataFrame({"lower": lower.round(2), "upper": upper.round(2)}))

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
