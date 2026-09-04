dataviz.classification.calibration_extra.platt_isotonic_overlay_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: platt_isotonic_overlay_interactive

Use case
--------

Use when choosing a recalibration method by comparing raw, Platt-scaled and isotonic mappings against binned observations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.calibration_extra import platt_isotonic_overlay_interactive

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   fig = platt_isotonic_overlay_interactive(y_true, y_prob)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration_extra/platt_isotonic_overlay_interactive.png" alt="platt_isotonic_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
