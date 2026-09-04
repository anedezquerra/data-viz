dataviz.classification.calibration.brier_score_bar_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration</p></div>

.. currentmodule:: dataviz.classification.calibration

.. autofunction:: brier_score_bar_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.calibration import brier_score_bar_interactive

   scores = {"Logistic regression": 0.089, "Random forest": 0.076, "Gradient boosting": 0.081}

   fig = brier_score_bar_interactive(scores)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/calibration/brier_score_bar_interactive.png" alt="brier_score_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
