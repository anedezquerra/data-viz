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
   import pandas as pd
   from dataviz.regression.diagnostics_panel import regression_dashboard_interactive

   rng = np.random.default_rng(42)
   n = 32
   actual = pd.Series(rng.uniform(15, 90, n), name="actual_wait_min")
   predicted = pd.Series(actual + rng.normal(0, 6, n), name="predicted_wait_min")

   fig = regression_dashboard_interactive(
       actual, predicted, n_features=4,
       title="Clinic Wait-Time Model: Performance Dashboard",
       color="#2a7f62", line_color="#c0392b", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/diagnostics_panel/regression_dashboard_interactive.png" alt="regression_dashboard_interactive example output"><figcaption>Example output</figcaption></figure></div>
