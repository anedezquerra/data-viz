dataviz.xai.local_more.prototype_criticism_grid_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: prototype_criticism_grid_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.local_more import prototype_criticism_grid_interactive

   prototypes = pd.DataFrame(
       {"income": [35.0, 60.0], "debt": [5.0, 12.0], "tenure": [1.0, 6.0]}
   )
   criticisms = pd.DataFrame(
       {"income": [48.0], "debt": [20.0], "tenure": [2.5]}
   )

   fig = prototype_criticism_grid_interactive(prototypes, criticisms)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/prototype_criticism_grid_interactive.png" alt="prototype_criticism_grid_interactive example output"><figcaption>Example output</figcaption></figure></div>
