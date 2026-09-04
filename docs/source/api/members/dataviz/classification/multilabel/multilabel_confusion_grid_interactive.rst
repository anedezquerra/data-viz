dataviz.classification.multilabel.multilabel_confusion_grid_interactive
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multilabel</p></div>

.. currentmodule:: dataviz.classification.multilabel

.. autofunction:: multilabel_confusion_grid_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.multilabel import multilabel_confusion_grid_interactive

   rng = np.random.default_rng(42)
   Y_true = rng.binomial(1, 0.4, size=(120, 4))
   Y_pred = rng.binomial(1, 0.4, size=(120, 4))

   fig = multilabel_confusion_grid_interactive(Y_true, Y_pred, labels=["sports", "tech", "politics", "health"])
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multilabel/multilabel_confusion_grid_interactive.png" alt="multilabel_confusion_grid_interactive example output"><figcaption>Example output</figcaption></figure></div>
