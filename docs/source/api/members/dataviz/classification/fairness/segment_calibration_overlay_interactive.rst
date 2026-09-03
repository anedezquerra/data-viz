dataviz.classification.fairness.segment_calibration_overlay_interactive
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.fairness</p></div>

.. currentmodule:: dataviz.classification.fairness

.. autofunction:: segment_calibration_overlay_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.fairness import segment_calibration_overlay_interactive

   rng = np.random.default_rng(42)
   groups = rng.choice(["Group A", "Group B"], size=200)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   fig = segment_calibration_overlay_interactive(y_true, y_prob, groups)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/fairness/segment_calibration_overlay_interactive.png" alt="segment_calibration_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
