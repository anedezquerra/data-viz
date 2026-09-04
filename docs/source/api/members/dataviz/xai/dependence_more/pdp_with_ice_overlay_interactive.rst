dataviz.xai.dependence_more.pdp_with_ice_overlay_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: pdp_with_ice_overlay_interactive

Use case
--------

Use to show the average feature effect while revealing heterogeneous per-instance behavior hidden by a plain PDP.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.dependence_more import pdp_with_ice_overlay_interactive

   rng = np.random.default_rng(42)
   grid = np.linspace(300, 850, 30)
   base = 1.0 / (1.0 + np.exp((grid - 600.0) / 70.0))
   offsets = rng.normal(0.0, 0.08, size=(40, 1))
   ice_curves = base[None, :] + offsets + rng.normal(0.0, 0.02, size=(40, grid.size))
   pdp = ice_curves.mean(axis=0)
   rug = rng.uniform(300, 850, size=25)

   fig = pdp_with_ice_overlay_interactive(
       grid,
       ice_curves,
       pdp,
       feature_name="Credit score",
       title="PDP + ICE: Default Risk vs Credit Score",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/dependence_more/pdp_with_ice_overlay_interactive.png" alt="pdp_with_ice_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
