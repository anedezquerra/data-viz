dataviz.univariate.distribution.pp_plot_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: pp_plot_interactive

Use case
--------

Use to compare cumulative probabilities between data and a theoretical distribution to check fit near the center.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.distribution import pp_plot_interactive

   # Machine cycle times fitted against a gamma reference
   rng = np.random.default_rng(42)
   cycle_s = pd.Series(
       np.round(rng.gamma(shape=5.0, scale=2.1, size=52), 2),
       name="cycle_s",
   )

   fig = pp_plot_interactive(
       cycle_s,
       distribution="gamma",
       title="Cycle Time PP Plot (Gamma)",
       color="darkslategray",
       reference_color="crimson",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/pp_plot_interactive.png" alt="pp_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
