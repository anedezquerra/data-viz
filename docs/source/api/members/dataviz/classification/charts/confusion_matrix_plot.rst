dataviz.classification.charts.confusion_matrix_plot
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.charts</p></div>

.. currentmodule:: dataviz.classification.charts

.. autofunction:: confusion_matrix_plot

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.charts import confusion_matrix_plot

   cm = np.array([[32, 4], [5, 29]])
   fpr = np.array([0.0, 0.1, 0.3, 1.0])
   tpr = np.array([0.0, 0.7, 0.9, 1.0])
   precision = np.array([1.0, 0.86, 0.72])
   recall = np.array([0.2, 0.7, 1.0])

   result = confusion_matrix_plot(cm)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/charts/confusion_matrix_plot.png" alt="confusion_matrix_plot example output"><figcaption>Example output</figcaption></figure></div>
