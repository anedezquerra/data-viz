dataviz.classification.training.training_history_curve_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.training</p></div>

.. currentmodule:: dataviz.classification.training

.. autofunction:: training_history_curve_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.training import training_history_curve_static

   history = {
       "loss": [0.90, 0.62, 0.45, 0.36, 0.30, 0.27],
       "val_loss": [0.95, 0.70, 0.55, 0.50, 0.51, 0.53],
   }

   ax = training_history_curve_static(history)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/training/training_history_curve_static.png" alt="training_history_curve_static example output"><figcaption>Example output</figcaption></figure></div>
