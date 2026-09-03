dataviz.multivariate.parallel.parallel_coordinates_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.multivariate.parallel</p></div>

.. currentmodule:: dataviz.multivariate.parallel

.. autofunction:: parallel_coordinates_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.multivariate.parallel import parallel_coordinates_static

   df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [4, 3, 2, 1], "segment": ["A", "A", "B", "B"]})

   ax = parallel_coordinates_static(df)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/multivariate/parallel/parallel_coordinates_static.png" alt="parallel_coordinates_static example output"><figcaption>Example output</figcaption></figure></div>
