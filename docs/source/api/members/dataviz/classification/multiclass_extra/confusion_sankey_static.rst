dataviz.classification.multiclass_extra.confusion_sankey_static
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass_extra</p></div>

.. currentmodule:: dataviz.classification.multiclass_extra

.. autofunction:: confusion_sankey_static

Use case
--------

Use to see where examples flow from true to predicted classes; band width shows which confusions dominate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass_extra import confusion_sankey_static

   rng = np.random.default_rng(42)
   # 3-stage fault classifier: true vs predicted flow
   n = 120
   labels = ["minor", "major", "critical"]
   y_true = np.array([labels[i] for i in rng.integers(0, 3, n)])
   flip = rng.random(n) < 0.18  # 18% of cases are misclassified
   y_pred = y_true.copy()
   y_pred[flip] = np.array([labels[i] for i in rng.integers(0, 3, flip.sum())])

   ax = confusion_sankey_static(y_true, y_pred, labels=labels,
                                title="Fault triage: true vs predicted flow")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass_extra/confusion_sankey_static.png" alt="confusion_sankey_static example output"><figcaption>Example output</figcaption></figure></div>
