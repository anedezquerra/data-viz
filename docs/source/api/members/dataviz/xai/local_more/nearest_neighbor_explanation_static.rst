dataviz.xai.local_more.nearest_neighbor_explanation_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: nearest_neighbor_explanation_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.local_more import nearest_neighbor_explanation_static

   query = {"income": 52.0, "debt": 8.0, "tenure": 4.0}
   neighbors = pd.DataFrame(
       {
           "income": [50.0, 55.0, 49.0],
           "debt": [9.0, 7.5, 10.0],
           "tenure": [3.5, 4.5, 4.0],
       }
   )
   target = [1, 1, 0]

   ax = nearest_neighbor_explanation_static(query, neighbors, target=target)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/nearest_neighbor_explanation_static.png" alt="nearest_neighbor_explanation_static example output"><figcaption>Example output</figcaption></figure></div>
