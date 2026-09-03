dataviz.xai.local_more.prototype_criticism_grid_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: prototype_criticism_grid_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.local_more import prototype_criticism_grid_static

   prototypes = pd.DataFrame(
       {"income": [35.0, 60.0], "debt": [5.0, 12.0], "tenure": [1.0, 6.0]}
   )
   criticisms = pd.DataFrame(
       {"income": [48.0], "debt": [20.0], "tenure": [2.5]}
   )

   ax = prototype_criticism_grid_static(prototypes, criticisms)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/local_more/prototype_criticism_grid_static.png" alt="prototype_criticism_grid_static example output"><figcaption>Example output</figcaption></figure></div>
