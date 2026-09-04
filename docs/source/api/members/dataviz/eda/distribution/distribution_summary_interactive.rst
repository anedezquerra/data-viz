dataviz.eda.distribution.distribution_summary_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.eda.distribution</p></div>

.. currentmodule:: dataviz.eda.distribution

.. autofunction:: distribution_summary_interactive

Use case
--------

Use at the start of exploratory analysis to review the distribution of every dataframe column at once.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.eda.distribution import distribution_summary_interactive

   rng = np.random.default_rng(42)
   n = 120
   df = pd.DataFrame({
       "Order value (USD)": rng.lognormal(mean=4.0, sigma=0.5, size=n),
       "Items per order": rng.poisson(lam=3.0, size=n),
       "Discount (%)": rng.uniform(low=0.0, high=25.0, size=n),
       "Delivery days": rng.integers(1, 10, size=n).astype(float),
   })

   fig = distribution_summary_interactive(
       df,
       title="Order Metrics Distribution Summary",
       bins=25,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/eda/distribution/distribution_summary_interactive.png" alt="distribution_summary_interactive example output"><figcaption>Example output</figcaption></figure></div>
