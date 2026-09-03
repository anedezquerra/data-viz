dataviz.classification.confusion_extended.confusion_matrix_diff_static
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.confusion_extended</p></div>

.. currentmodule:: dataviz.classification.confusion_extended

.. autofunction:: confusion_matrix_diff_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.confusion_extended import confusion_matrix_diff_static

   cm_a = np.array([[32, 4], [5, 29]])
   cm_b = np.array([[28, 8], [7, 27]])

   ax = confusion_matrix_diff_static(cm_a, cm_b)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/confusion_extended/confusion_matrix_diff_static.png" alt="confusion_matrix_diff_static example output"><figcaption>Example output</figcaption></figure></div>
