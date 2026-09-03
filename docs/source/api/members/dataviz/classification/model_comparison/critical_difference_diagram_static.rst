dataviz.classification.model_comparison.critical_difference_diagram_static
==========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: critical_difference_diagram_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.model_comparison import critical_difference_diagram_static

   rank_table = {
       "Logistic regression": [2, 3, 1, 2, 3, 2],
       "Random forest": [1, 1, 2, 1, 1, 1],
       "Gradient boosting": [3, 2, 3, 3, 2, 3],
   }

   ax = critical_difference_diagram_static(rank_table, cd=1.2)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/model_comparison/critical_difference_diagram_static.png" alt="critical_difference_diagram_static example output"><figcaption>Example output</figcaption></figure></div>
