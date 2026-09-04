dataviz.regression.autocorrelation.residual_runs_plot_interactive
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.autocorrelation</p></div>

.. currentmodule:: dataviz.regression.autocorrelation

.. autofunction:: residual_runs_plot_interactive

Use case
--------

Use to spot non-random runs of positive or negative residuals, a quick check for structure the model failed to capture.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.autocorrelation import residual_runs_plot_interactive

   rng = np.random.default_rng(42)
   run = np.arange(28)
   strength = pd.Series(32 + 0.15 * run + rng.normal(0, 0.9, 28),
                        name="tensile_strength_mpa")
   fitted = pd.Series(np.full(28, 32.0 + 0.15 * 13.5), name="mean_only_fit")

   fig = residual_runs_plot_interactive(strength, fitted,
                                        title="Tensile Strength: Residual Runs Chart",
                                        positive_color="#2a7f62",
                                        negative_color="#c0392b",
                                        template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/autocorrelation/residual_runs_plot_interactive.png" alt="residual_runs_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
