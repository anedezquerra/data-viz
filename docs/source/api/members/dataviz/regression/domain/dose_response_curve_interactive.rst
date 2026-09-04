dataviz.regression.domain.dose_response_curve_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.domain</p></div>

.. currentmodule:: dataviz.regression.domain

.. autofunction:: dose_response_curve_interactive

Use case
--------

Use in pharmacology or toxicology to plot response versus dose with an optional CI band and log-scaled dose axis.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.domain import dose_response_curve_interactive

   rng = np.random.default_rng(42)
   dose = pd.Series(np.logspace(-1, 2, 14), name="dose_mg")
   response = pd.Series(100 / (1 + (dose / 12) ** -1.1) + rng.normal(0, 3, 14),
                        name="response_pct")
   lo = response - 6.0
   hi = response + 6.0

   fig = dose_response_curve_interactive(dose, response, lower=lo, upper=hi,
                                         title="Compound B: Dose-Response (EC50)",
                                         color="#2a7f62",
                                         template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/domain/dose_response_curve_interactive.png" alt="dose_response_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
