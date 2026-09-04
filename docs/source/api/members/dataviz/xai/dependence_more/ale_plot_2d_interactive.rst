dataviz.xai.dependence_more.ale_plot_2d_interactive
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: ale_plot_2d_interactive

Use case
--------

Use to visualize the joint effect of two correlated features without the extrapolation bias of 2-D PDPs.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.dependence_more import ale_plot_2d_interactive

   rng = np.random.default_rng(42)
   x_edges = np.linspace(300, 850, 11)
   y_edges = np.linspace(0.0, 0.6, 9)
   xc = 0.5 * (x_edges[:-1] + x_edges[1:])
   yc = 0.5 * (y_edges[:-1] + y_edges[1:])
   ale_grid = (
       -0.4 * np.exp(-(((xc[:, None] - 580.0) / 90.0) ** 2)) * (1.0 + yc[None, :])
       + 0.15 * (yc[None, :] - 0.3)
       + rng.normal(0.0, 0.01, size=(len(xc), len(yc)))
   )

   fig = ale_plot_2d_interactive(
       ale_grid,
       x_edges,
       y_edges,
       feature_x="Credit score",
       feature_y="Utilization",
       title="2-D ALE: Credit Score x Utilization Interaction Effect",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/dependence_more/ale_plot_2d_interactive.png" alt="ale_plot_2d_interactive example output"><figcaption>Example output</figcaption></figure></div>
