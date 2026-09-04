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
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.diagnostics_panel import regression_diagnostic_panel_static

   rng = np.random.default_rng(42)
   n = 30
   X = pd.DataFrame({
       "temperature_c": rng.uniform(15, 35, n),
       "rainfall_mm": rng.uniform(200, 1200, n),
       "fertilizer_kg": rng.uniform(50, 300, n),
   })
   y = pd.Series(2.1 * X["temperature_c"] + 0.004 * X["rainfall_mm"]
                 + 0.015 * X["fertilizer_kg"] + rng.normal(0, 4, n),
                 name="yield_t_ha")
   fitted = pd.Series(2.1 * X["temperature_c"] + 0.004 * X["rainfall_mm"]
                      + 0.015 * X["fertilizer_kg"], name="fitted")

   fig = regression_diagnostic_panel_static(
       X, y, fitted, title="Crop Yield Model: Diagnostic Panel",
       color="#1f6fb2", line_color="#c0392b")
   fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/diagnostics_panel/regression_diagnostic_panel_static.png" alt="regression_diagnostic_panel_static example output"><figcaption>Example output</figcaption></figure></div>
