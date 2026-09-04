dataviz.classification.confusion_extended.error_analysis_grid_interactive
=========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.confusion_extended</p></div>

.. currentmodule:: dataviz.classification.confusion_extended

.. autofunction:: error_analysis_grid_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.confusion_extended import error_analysis_grid_interactive

   cm = np.array([[32, 4], [5, 29]])
   fpr = np.array([0.0, 0.1, 0.3, 1.0])
   tpr = np.array([0.0, 0.7, 0.9, 1.0])
   precision = np.array([1.0, 0.86, 0.72])
   recall = np.array([0.2, 0.7, 1.0])

   fig = error_analysis_grid_interactive(cm)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/confusion_extended/error_analysis_grid_interactive.png" alt="error_analysis_grid_interactive example output"><figcaption>Example output</figcaption></figure></div>
