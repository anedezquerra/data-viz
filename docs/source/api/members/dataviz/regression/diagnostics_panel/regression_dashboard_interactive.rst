dataviz.regression.diagnostics_panel.regression_dashboard_interactive
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.diagnostics_panel</p></div>

.. currentmodule:: dataviz.regression.diagnostics_panel

.. autofunction:: regression_dashboard_interactive

Use case
--------

Use for a compact model overview combining predicted-vs-actual, residual scatter, error histogram, and summary metrics.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.diagnostics_panel import regression_dashboard_interactive

   y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])
   y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])
   train_sizes = np.array([50, 100, 200])
   train_scores = np.array([0.82, 0.86, 0.89])
   validation_scores = np.array([0.76, 0.81, 0.84])

   fig = regression_dashboard_interactive(y_true, y_pred)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/diagnostics_panel/regression_dashboard_interactive.png" alt="regression_dashboard_interactive example output"><figcaption>Example output</figcaption></figure></div>
