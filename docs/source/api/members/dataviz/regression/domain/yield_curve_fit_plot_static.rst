dataviz.regression.domain.yield_curve_fit_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.domain</p></div>

.. currentmodule:: dataviz.regression.domain

.. autofunction:: yield_curve_fit_plot_static

Use case
--------

Use in fixed-income work to compare observed bond yields against a fitted curve across maturities and spot mispriced points.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.domain import yield_curve_fit_plot_static

   rng = np.random.default_rng(42)
   maturities = np.array([0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0])
   observed_yields = np.array([1.8, 2.0, 2.3, 2.6, 3.0, 3.2, 3.4])
   fitted_yields = observed_yields + rng.normal(0.0, 0.03, size=7)

   ax = yield_curve_fit_plot_static(maturities, observed_yields, fitted_yields)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/domain/yield_curve_fit_plot_static.png" alt="yield_curve_fit_plot_static example output"><figcaption>Example output</figcaption></figure></div>
