dataviz.classification.errors.misclassification_cluster_heatmap_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.errors</p></div>

.. currentmodule:: dataviz.classification.errors

.. autofunction:: misclassification_cluster_heatmap_interactive

Use case
--------

Use to localize errors by true class and score bin, revealing where in the score range mistakes concentrate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.errors import misclassification_cluster_heatmap_interactive

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   fig = misclassification_cluster_heatmap_interactive(y_true, y_prob)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/errors/misclassification_cluster_heatmap_interactive.png" alt="misclassification_cluster_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
