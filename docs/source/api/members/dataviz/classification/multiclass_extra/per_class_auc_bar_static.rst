dataviz.classification.multiclass_extra.per_class_auc_bar_static
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass_extra</p></div>

.. currentmodule:: dataviz.classification.multiclass_extra

.. autofunction:: per_class_auc_bar_static

Use case
--------

Use to spot weak classes at a glance; bars show per-class one-vs-rest AUC against the 0.5 random line.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass_extra import per_class_auc_bar_static

   # per-class one-vs-rest AUC from a 5-class document-topic classifier
   auc_per_class = {
       "sports": 0.94,
       "politics": 0.88,
       "tech": 0.91,
       "finance": 0.82,
       "culture": 0.76,
   }

   ax = per_class_auc_bar_static(auc_per_class,
                                 title="Topic classifier: per-class AUC",
                                 color="#2a6f97")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass_extra/per_class_auc_bar_static.png" alt="per_class_auc_bar_static example output"><figcaption>Example output</figcaption></figure></div>
