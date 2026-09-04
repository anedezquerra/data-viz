dataviz.univariate.distribution.qq_plot_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: qq_plot_interactive

Use case
--------

Use to compare sample quantiles against a theoretical distribution to assess fit, especially in the tails.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.distribution import qq_plot_interactive

   # Heights measured in a university anthropometry study
   rng = np.random.default_rng(42)
   height_cm = pd.Series(
       np.round(rng.normal(loc=171.0, scale=9.5, size=48), 1),
       name="height_cm",
   )

   fig = qq_plot_interactive(
       height_cm,
       distribution="norm",
       title="Height Normality QQ Plot",
       color="steelblue",
       reference_color="crimson",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/qq_plot_interactive.png" alt="qq_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
