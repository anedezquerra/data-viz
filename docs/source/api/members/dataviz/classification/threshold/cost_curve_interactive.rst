dataviz.classification.threshold.cost_curve_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold</p></div>

.. currentmodule:: dataviz.classification.threshold

.. autofunction:: cost_curve_interactive

Use case
--------

Use when false positives and false negatives carry different costs; finds the threshold minimizing total misclassification cost.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.threshold import cost_curve_interactive

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   fig = cost_curve_interactive(y_true, y_prob)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold/cost_curve_interactive.png" alt="cost_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
