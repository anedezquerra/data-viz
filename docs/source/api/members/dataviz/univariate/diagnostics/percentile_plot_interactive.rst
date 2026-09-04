dataviz.univariate.diagnostics.percentile_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.diagnostics</p></div>

.. currentmodule:: dataviz.univariate.diagnostics

.. autofunction:: percentile_plot_interactive

Use case
--------

Use to profile a variable across its percentiles, revealing tail behavior and skew beyond mean and standard deviation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.diagnostics import percentile_plot_interactive

   # Response times for an internal API endpoint over one day
   rng = np.random.default_rng(42)
   response_ms = pd.Series(
       np.round(rng.lognormal(mean=4.6, sigma=0.5, size=58), 1),
       name="response_ms",
   )

   fig = percentile_plot_interactive(
       response_ms,
       step=10,
       title="API Response Time Percentile Profile",
       xlabel="Percentile",
       ylabel="Response Time (ms)",
       color="darkmagenta",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/diagnostics/percentile_plot_interactive.png" alt="percentile_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
