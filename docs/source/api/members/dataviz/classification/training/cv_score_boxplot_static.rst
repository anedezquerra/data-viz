dataviz.classification.training.cv_score_boxplot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.training</p></div>

.. currentmodule:: dataviz.classification.training

.. autofunction:: cv_score_boxplot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.training import cv_score_boxplot_static

   cv_scores = {
       "Logistic regression": [0.81, 0.83, 0.80, 0.82, 0.84],
       "Random forest": [0.87, 0.89, 0.88, 0.86, 0.90],
       "Gradient boosting": [0.85, 0.87, 0.86, 0.88, 0.87],
   }

   ax = cv_score_boxplot_static(cv_scores)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/training/cv_score_boxplot_static.png" alt="cv_score_boxplot_static example output"><figcaption>Example output</figcaption></figure></div>
