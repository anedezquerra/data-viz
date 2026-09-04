dataviz.classification.multiclass_extra.top_k_accuracy_curve_static
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass_extra</p></div>

.. currentmodule:: dataviz.classification.multiclass_extra

.. autofunction:: top_k_accuracy_curve_static

Use case
--------

Use when predictions feed a downstream re-ranker; shows how accuracy grows as the top-K candidate set widens.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass_extra import top_k_accuracy_curve_static

   rng = np.random.default_rng(42)
   # 6-class product recommender: does the right item appear in the top-K?
   n = 120
   n_classes = 6
   y_true = rng.integers(0, n_classes, n)
   logits = rng.normal(0, 1, (n, n_classes))
   logits[np.arange(n), y_true] += 2.2  # model signal on the true class
   probs = np.exp(logits) / np.exp(logits).sum(axis=1, keepdims=True)

   ax = top_k_accuracy_curve_static(y_true, probs,
                                    title="Recommender top-K accuracy")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass_extra/top_k_accuracy_curve_static.png" alt="top_k_accuracy_curve_static example output"><figcaption>Example output</figcaption></figure></div>
