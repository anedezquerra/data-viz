dataviz.univariate.distribution.cumulative_histogram_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: cumulative_histogram_interactive

Use case
--------

Use to show cumulative counts across bins when the running total of observations matters more than per-bin frequency.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.distribution import cumulative_histogram_interactive

   # Order values processed by an online checkout during a sale
   rng = np.random.default_rng(42)
   order_usd = pd.Series(
       np.round(rng.lognormal(mean=4.2, sigma=0.6, size=54), 2),
       name="order_usd",
   )

   fig = cumulative_histogram_interactive(
       order_usd,
       bins=15,
       title="Cumulative Order Value Distribution",
       xlabel="Order Value (USD)",
       ylabel="Cumulative Orders",
       color="goldenrod",
       alpha=0.8,
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/cumulative_histogram_interactive.png" alt="cumulative_histogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
