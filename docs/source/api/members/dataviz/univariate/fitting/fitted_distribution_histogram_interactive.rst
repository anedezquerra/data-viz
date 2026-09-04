dataviz.univariate.fitting.fitted_distribution_histogram_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.fitting</p></div>

.. currentmodule:: dataviz.univariate.fitting

.. autofunction:: fitted_distribution_histogram_interactive

Use case
--------

Use to overlay a fitted probability density on a histogram to visually judge how well the chosen distribution fits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.fitting import fitted_distribution_histogram_interactive

   # Insurance claim severities recorded by an auto portfolio
   rng = np.random.default_rng(42)
   claims = pd.Series(
       np.round(rng.lognormal(mean=8.1, sigma=0.9, size=56), 0),
       name="claim_usd",
   )

   fig = fitted_distribution_histogram_interactive(
       claims,
       distribution="lognorm",
       bins=16,
       title="Claim Severity with Fitted Lognormal",
       xlabel="Claim Amount (USD)",
       color="lightsteelblue",
       fit_color="crimson",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/fitting/fitted_distribution_histogram_interactive.png" alt="fitted_distribution_histogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
