dataviz.bivariate.trends.binned_mean_plot_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.trends</p></div>

.. currentmodule:: dataviz.bivariate.trends

.. autofunction:: binned_mean_plot_interactive

Use case
--------

Use to smooth noisy scatter data into mean y values per x bin and reveal the underlying trend.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.trends import binned_mean_plot_interactive

   rng = np.random.default_rng(42)
   n = 160
   depth = pd.Series(rng.uniform(low=0.0, high=200.0, size=n), name="Depth (m)")
   temperature = pd.Series(25.0 - 0.08 * depth + rng.normal(loc=0.0, scale=1.5, size=n), name="Water temperature (C)")

   fig = binned_mean_plot_interactive(
       depth,
       temperature,
       bins=8,
       title="Mean Water Temperature by Depth Bin",
       color="darkcyan",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/trends/binned_mean_plot_interactive.png" alt="binned_mean_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
