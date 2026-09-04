dataviz.regression.gof.white_test_plot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.gof</p></div>

.. currentmodule:: dataviz.regression.gof

.. autofunction:: white_test_plot_interactive

Use case
--------

Use to screen for heteroscedasticity with the White test across predictors without assuming a specific form.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.gof import white_test_plot_interactive

   rng = np.random.default_rng(42)
   n = 36
   machine_speed = rng.uniform(200.0, 900.0, n)
   tool_age_hrs = rng.uniform(10.0, 500.0, n)
   X = pd.DataFrame({"machine_speed_rpm": machine_speed,
                      "tool_age_hrs": tool_age_hrs})
   residuals = pd.Series(rng.normal(0.0, 0.5 + 0.002 * machine_speed, n),
                         name="roughness_residuals_um")

   fig = white_test_plot_interactive(X, residuals,
                                     title="Milling Line: White Heteroscedasticity Test",
                                     template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/gof/white_test_plot_interactive.png" alt="white_test_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
