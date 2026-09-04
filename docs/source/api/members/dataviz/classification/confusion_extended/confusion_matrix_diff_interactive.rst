dataviz.classification.confusion_extended.confusion_matrix_diff_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.confusion_extended</p></div>

.. currentmodule:: dataviz.classification.confusion_extended

.. autofunction:: confusion_matrix_diff_interactive

Use case
--------

Compare two models by plotting the element-wise difference of their confusion matrices to see where errors shift.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.confusion_extended import confusion_matrix_diff_interactive

   cm_a = np.array([[32, 4], [5, 29]])
   cm_b = np.array([[28, 8], [7, 27]])

   fig = confusion_matrix_diff_interactive(cm_a, cm_b)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/confusion_extended/confusion_matrix_diff_interactive.png" alt="confusion_matrix_diff_interactive example output"><figcaption>Example output</figcaption></figure></div>
