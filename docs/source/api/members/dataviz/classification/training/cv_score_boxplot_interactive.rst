dataviz.classification.training.cv_score_boxplot_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.training</p></div>

.. currentmodule:: dataviz.classification.training

.. autofunction:: cv_score_boxplot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.training import cv_score_boxplot_interactive

   cv_scores = {
       "Logistic regression": [0.81, 0.83, 0.80, 0.82, 0.84],
       "Random forest": [0.87, 0.89, 0.88, 0.86, 0.90],
       "Gradient boosting": [0.85, 0.87, 0.86, 0.88, 0.87],
   }

   fig = cv_score_boxplot_interactive(cv_scores)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
