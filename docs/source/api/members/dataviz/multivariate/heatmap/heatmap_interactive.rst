dataviz.multivariate.heatmap.heatmap_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.heatmap</p></div>

.. currentmodule:: dataviz.multivariate.heatmap

.. autofunction:: heatmap_interactive

Use case
--------

Use to display a numeric matrix as color intensity when patterns across two dimensions matter.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.multivariate.heatmap import heatmap_interactive

   rng = np.random.default_rng(42)
   days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   hours = [f"{h}:00" for h in range(6, 22, 2)]
   traffic = rng.integers(50, 500, size=(len(days), len(hours))).astype(float)
   traffic[5:, :3] *= 0.4
   df = pd.DataFrame(traffic, index=days, columns=hours)

   fig = heatmap_interactive(
       df,
       title="Store Foot Traffic by Day and Hour",
       colorscale="YlOrRd",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/multivariate/heatmap/heatmap_interactive.png" alt="heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
