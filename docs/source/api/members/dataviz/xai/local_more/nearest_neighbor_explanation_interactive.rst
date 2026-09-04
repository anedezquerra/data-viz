dataviz.xai.local_more.nearest_neighbor_explanation_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: nearest_neighbor_explanation_interactive

Use case
--------

Use to justify a prediction by comparing the query row's feature values against its k nearest neighbors in a heatmap.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.local_more import nearest_neighbor_explanation_interactive

   query = {"income": 52.0, "debt": 8.0, "tenure": 4.0}
   neighbors = pd.DataFrame(
       {
           "income": [50.0, 55.0, 49.0],
           "debt": [9.0, 7.5, 10.0],
           "tenure": [3.5, 4.5, 4.0],
       }
   )
   target = [1, 1, 0]

   fig = nearest_neighbor_explanation_interactive(query, neighbors, target=target)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/nearest_neighbor_explanation_interactive.png" alt="nearest_neighbor_explanation_interactive example output"><figcaption>Example output</figcaption></figure></div>
