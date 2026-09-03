dataviz.classification.multiclass.multiclass_pr_curve_static
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: multiclass_pr_curve_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass import multiclass_pr_curve_static

   curves = {
       "Class 0": (np.array([0.0, 0.5, 1.0]), np.array([0.9, 0.85, 0.6])),
       "Class 1": (np.array([0.0, 0.5, 1.0]), np.array([0.8, 0.7, 0.5])),
       "Class 2": (np.array([0.0, 0.5, 1.0]), np.array([0.7, 0.6, 0.4])),
   }

   ax = multiclass_pr_curve_static(curves)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
