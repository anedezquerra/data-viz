dataviz.classification.threshold_extra.predictive_value_curve_interactive
=========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold_extra</p></div>

.. currentmodule:: dataviz.classification.threshold_extra

.. autofunction:: predictive_value_curve_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.threshold_extra import predictive_value_curve_interactive

   prevalences = np.linspace(0.01, 0.5, 25)

   fig = predictive_value_curve_interactive(0.85, 0.90, prevalences=prevalences)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold_extra/predictive_value_curve_interactive.png" alt="predictive_value_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
