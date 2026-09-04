dataviz.xai.concept.embedding_projection_plot_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: embedding_projection_plot_interactive

Use case
--------

Use to explore a 2-D embedding projection colored by class or feature value to spot clusters and outliers.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.concept import embedding_projection_plot_interactive

   rng = np.random.default_rng(42)
   segments = {
       "loyal": (-2.0, 0.5),
       "at-risk": (0.5, 2.0),
       "churned": (2.0, -1.5),
   }
   coords, labels = [], []
   for name, (cx, cy) in segments.items():
       pts = rng.normal([cx, cy], 0.6, size=(30, 2))
       coords.append(pts)
       labels.extend([name] * len(pts))
   coords = np.vstack(coords)
   hover_text = [f"customer segment: {s}" for s in labels]

   fig = embedding_projection_plot_interactive(
       coords,
       labels=labels,
       hover_text=hover_text,
       title="Customer Embedding Projection (UMAP 2-D) - Churn Model",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/concept/embedding_projection_plot_interactive.png" alt="embedding_projection_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
