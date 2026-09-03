dataviz.classification.multiclass.roc_curve_comparison_interactive
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass</p></div>

.. currentmodule:: dataviz.classification.multiclass

.. autofunction:: roc_curve_comparison_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.multiclass import roc_curve_comparison_interactive

   models = {
       "Logistic regression": (np.array([0.0, 0.1, 0.3, 1.0]), np.array([0.0, 0.7, 0.9, 1.0])),
       "Random forest": (np.array([0.0, 0.05, 0.2, 1.0]), np.array([0.0, 0.8, 0.95, 1.0])),
       "Gradient boosting": (np.array([0.0, 0.08, 0.25, 1.0]), np.array([0.0, 0.75, 0.92, 1.0])),
   }

   fig = roc_curve_comparison_interactive(models)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
