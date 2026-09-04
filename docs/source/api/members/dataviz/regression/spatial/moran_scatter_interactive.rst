dataviz.regression.spatial.moran_scatter_interactive
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.spatial</p></div>

.. currentmodule:: dataviz.regression.spatial

.. autofunction:: moran_scatter_interactive

Use case
--------

Use to test for spatial autocorrelation by plotting each standardized value against its spatial lag; the slope approximates Moran's I.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.spatial import moran_scatter_interactive

   rng = np.random.default_rng(42)
   n = 48  # continental US states
   base = rng.normal(0, 1, n)
   unemployment = 4.5 + 1.2 * base + rng.normal(0, 0.4, n)
   spatial_lag = 4.5 + 1.2 * (0.6 * base + 0.4 * rng.normal(0, 1, n))

   fig = moran_scatter_interactive(
       unemployment, spatial_lag,
       title="State unemployment: Moran scatter of spatial autocorrelation",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/spatial/moran_scatter_interactive.png" alt="moran_scatter_interactive example output"><figcaption>Example output</figcaption></figure></div>
