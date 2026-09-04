dataviz.regression.diagnostics_panel.regression_diagnostic_panel_interactive
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.diagnostics_panel</p></div>

.. currentmodule:: dataviz.regression.diagnostics_panel

.. autofunction:: regression_diagnostic_panel_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.diagnostics_panel import regression_diagnostic_panel_interactive

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(60, 3))
   y_true = rng.normal(10.0, 2.0, size=60)
   y_pred = y_true + rng.normal(0.0, 0.5, size=60)

   fig = regression_diagnostic_panel_interactive(X, y_true, y_pred)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/diagnostics_panel/regression_diagnostic_panel_interactive.png" alt="regression_diagnostic_panel_interactive example output"><figcaption>Example output</figcaption></figure></div>
