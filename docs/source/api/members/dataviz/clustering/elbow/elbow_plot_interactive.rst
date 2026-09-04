dataviz.clustering.elbow.elbow_plot_interactive
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.clustering.elbow</p></div>

.. currentmodule:: dataviz.clustering.elbow

.. autofunction:: elbow_plot_interactive

Use case
--------

Use when choosing k for k-means by looking for the bend where added clusters stop reducing inertia much.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.clustering.elbow import elbow_plot_interactive

   n_clusters = np.arange(1, 11)
   inertias = np.array([520.0, 210.0, 120.0, 90.0, 74.0, 66.0, 61.0, 57.0, 54.0, 52.0])

   fig = elbow_plot_interactive(
       n_clusters,
       inertias,
       title="K-Means Elbow Plot",
       line_color="darkslateblue",
       elbow_idx=2,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/clustering/elbow/elbow_plot_interactive.png" alt="elbow_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
