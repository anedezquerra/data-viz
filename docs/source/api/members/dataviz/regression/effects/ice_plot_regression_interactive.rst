dataviz.regression.effects.ice_plot_regression_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: ice_plot_regression_interactive

Use case
--------

Use to reveal heterogeneous feature effects hidden by PDP: per-observation ICE lines with the average overlaid.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.effects import ice_plot_regression_interactive

   rng = np.random.default_rng(42)
   grid = np.linspace(0, 40, 20)
   ice = np.vstack([50 + 1.8 * grid + rng.normal(0, 8) + 0.02 * grid ** 2
                    for _ in range(15)])

   fig = ice_plot_regression_interactive(grid, ice,
                                         title="ICE: Commute Distance on Rent",
                                         feature_name="distance to downtown (km)",
                                         opacity=0.25, template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/ice_plot_regression_interactive.png" alt="ice_plot_regression_interactive example output"><figcaption>Example output</figcaption></figure></div>
