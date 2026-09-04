dataviz.univariate.inference.bootstrap_distribution_plot_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.inference</p></div>

.. currentmodule:: dataviz.univariate.inference

.. autofunction:: bootstrap_distribution_plot_interactive

Use case
--------

Use to visualize the bootstrap distribution of a statistic with the observed estimate marked, to judge stability and skew of the interval.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.inference import bootstrap_distribution_plot_interactive

   rng = np.random.default_rng(42)
   wait_minutes = pd.Series(
       rng.lognormal(mean=2.2, sigma=0.6, size=180).round(1),
       name="wait_minutes",
   )
   fig = bootstrap_distribution_plot_interactive(
       wait_minutes,
       statistic="mean",
       n_resamples=1000,
       seed=7,
       title="Bootstrap Mean Wait Time (Call Center)",
       color="steelblue",
       height=500,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/inference/bootstrap_distribution_plot_interactive.png" alt="bootstrap_distribution_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
