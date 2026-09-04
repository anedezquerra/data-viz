dataviz.classification.multiclass_extra.per_class_ap_bar_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass_extra</p></div>

.. currentmodule:: dataviz.classification.multiclass_extra

.. autofunction:: per_class_ap_bar_interactive

Use case
--------

Use to rank classes by Average Precision and find classes whose ranking quality drags down a multiclass model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.multiclass_extra import per_class_ap_bar_interactive

   ap_per_class = {"Class 0": 0.88, "Class 1": 0.79, "Class 2": 0.71}

   fig = per_class_ap_bar_interactive(ap_per_class)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass_extra/per_class_ap_bar_interactive.png" alt="per_class_ap_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
