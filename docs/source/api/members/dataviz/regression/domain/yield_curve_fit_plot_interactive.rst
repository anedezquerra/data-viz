dataviz.regression.domain.yield_curve_fit_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.domain</p></div>

.. currentmodule:: dataviz.regression.domain

.. autofunction:: yield_curve_fit_plot_interactive

Use case
--------

Use in fixed-income work to compare observed bond yields against a fitted curve across maturities and spot mispriced points.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.domain import yield_curve_fit_plot_interactive

   rng = np.random.default_rng(42)
   maturities = pd.Series([0.25, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30],
                          name="maturity_years")
   observed = pd.Series(4.2 - 1.8 * np.exp(-maturities / 3)
                        + rng.normal(0, 0.05, maturities.size), name="yield_pct")
   fitted = pd.Series(4.2 - 1.8 * np.exp(-maturities / 3), name="fitted_pct")

   fig = yield_curve_fit_plot_interactive(maturities, observed, fitted,
                                          title="Treasury Yield Curve: Nelson-Siegel Fit",
                                          obs_color="#1f6fb2", fit_color="#c0392b",
                                          template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/domain/yield_curve_fit_plot_interactive.png" alt="yield_curve_fit_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
