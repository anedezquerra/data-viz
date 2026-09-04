dataviz.classification.multiclass_extra.per_class_auc_bar_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass_extra</p></div>

.. currentmodule:: dataviz.classification.multiclass_extra

.. autofunction:: per_class_auc_bar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass_extra import per_class_auc_bar_static

   auc_per_class = {"Class 0": 0.92, "Class 1": 0.85, "Class 2": 0.78}

   ax = per_class_auc_bar_static(auc_per_class)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass_extra/per_class_auc_bar_static.png" alt="per_class_auc_bar_static example output"><figcaption>Example output</figcaption></figure></div>
