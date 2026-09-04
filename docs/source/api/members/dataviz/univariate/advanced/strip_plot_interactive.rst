dataviz.univariate.advanced.strip_plot_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: strip_plot_interactive

Use case
--------

Use to display each observation as a jittered point, ideal for small samples where exact values and density matter.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.advanced import strip_plot_interactive

   # Daily coffee-shop transaction amounts over six weeks
   rng = np.random.default_rng(42)
   amounts = pd.Series(
       np.round(rng.gamma(shape=4.0, scale=1.8, size=42), 2),
       name="transaction_usd",
   )

   fig = strip_plot_interactive(
       amounts,
       title="Individual Transaction Amounts",
       ylabel="Amount (USD)",
       color="darkorange",
       jitter=0.12,
       seed=7,
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/strip_plot_interactive.png" alt="strip_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
