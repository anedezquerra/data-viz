dataviz.univariate.distribution.ecdf_plot_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: ecdf_plot_interactive

Use case
--------

Use to plot the empirical cumulative distribution, reading off medians and quantiles directly without binning.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.distribution import ecdf_plot_interactive

   # Rental durations for a bike-share station over one week
   rng = np.random.default_rng(42)
   duration_min = pd.Series(
       np.round(rng.gamma(shape=2.2, scale=9.0, size=38), 1),
       name="rental_min",
   )

   fig = ecdf_plot_interactive(
       duration_min,
       title="Bike-Share Rental Duration ECDF",
       xlabel="Rental Duration (min)",
       color="darkgreen",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/distribution/ecdf_plot_interactive.png" alt="ecdf_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
