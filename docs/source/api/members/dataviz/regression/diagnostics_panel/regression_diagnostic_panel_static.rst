dataviz.regression.diagnostics_panel.regression_diagnostic_panel_static
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.diagnostics_panel</p></div>

.. currentmodule:: dataviz.regression.diagnostics_panel

.. autofunction:: regression_diagnostic_panel_static

Use case
--------

Use as a one-shot check of classic OLS assumptions: residuals-vs-fitted, QQ, scale-location, and leverage in four panels.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.diagnostics_panel import regression_diagnostic_panel_static

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(60, 3))
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)

   result = regression_diagnostic_panel_static(X, y_true, y_pred)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/diagnostics_panel/regression_diagnostic_panel_static.png" alt="regression_diagnostic_panel_static example output"><figcaption>Example output</figcaption></figure></div>
