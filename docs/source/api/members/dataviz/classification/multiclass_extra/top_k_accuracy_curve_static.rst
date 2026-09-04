dataviz.classification.multiclass_extra.top_k_accuracy_curve_static
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass_extra</p></div>

.. currentmodule:: dataviz.classification.multiclass_extra

.. autofunction:: top_k_accuracy_curve_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass_extra import top_k_accuracy_curve_static

   rng = np.random.default_rng(42)
   logits = rng.normal(size=(200, 4))
   exp_logits = np.exp(logits - logits.max(axis=1, keepdims=True))
   y_prob_matrix = exp_logits / exp_logits.sum(axis=1, keepdims=True)
   y_true = rng.choice(4, size=200)

   ax = top_k_accuracy_curve_static(y_true, y_prob_matrix)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/multiclass_extra/top_k_accuracy_curve_static.png" alt="top_k_accuracy_curve_static example output"><figcaption>Example output</figcaption></figure></div>
