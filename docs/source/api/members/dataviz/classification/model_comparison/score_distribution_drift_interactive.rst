dataviz.classification.model_comparison.score_distribution_drift_interactive
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: score_distribution_drift_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.model_comparison import score_distribution_drift_interactive

   rng = np.random.default_rng(42)
   scores_reference = rng.beta(2.0, 5.0, size=400)
   scores_current = rng.beta(2.5, 4.5, size=400)

   fig = score_distribution_drift_interactive(scores_reference, scores_current)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/score_distribution_drift_interactive.png" alt="score_distribution_drift_interactive example output"><figcaption>Example output</figcaption></figure></div>
