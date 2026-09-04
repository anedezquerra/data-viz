dataviz.univariate.advanced.rug_plot_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: rug_plot_interactive

Use case
--------

Use to show every individual observation as ticks along an axis, revealing clustering and gaps that bins can hide.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.advanced import rug_plot_interactive

   # Packet round-trip times captured on a network link
   rng = np.random.default_rng(42)
   latency_ms = pd.Series(
       np.round(rng.lognormal(mean=3.4, sigma=0.35, size=45), 1),
       name="latency_ms",
   )

   fig = rug_plot_interactive(
       latency_ms,
       title="Round-Trip Latency Observations",
       xlabel="Latency (ms)",
       color="steelblue",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/rug_plot_interactive.png" alt="rug_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
