dataviz.xai.dependence_more.h_statistic_heatmap_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: h_statistic_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.dependence_more import h_statistic_heatmap_static

   h_matrix = pd.DataFrame(
       [[1.0, 0.32, 0.05], [0.32, 1.0, 0.11], [0.05, 0.11, 1.0]],
       index=["age", "income", "tenure"],
       columns=["age", "income", "tenure"],
   )

   ax = h_statistic_heatmap_static(h_matrix)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/dependence_more/h_statistic_heatmap_static.png" alt="h_statistic_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
