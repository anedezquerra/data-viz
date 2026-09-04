dataviz.classification.multiclass.multiclass_pr_curve_interactive
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: multiclass_pr_curve_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.multiclass import multiclass_pr_curve_interactive

   curves = {
       "Class 0": (np.array([0.0, 0.5, 1.0]), np.array([0.9, 0.85, 0.6])),
       "Class 1": (np.array([0.0, 0.5, 1.0]), np.array([0.8, 0.7, 0.5])),
       "Class 2": (np.array([0.0, 0.5, 1.0]), np.array([0.7, 0.6, 0.4])),
   }

   fig = multiclass_pr_curve_interactive(curves)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass/multiclass_pr_curve_interactive.png" alt="multiclass_pr_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
