dataviz.classification.multilabel.label_cooccurrence_heatmap_static
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multilabel</p></div>

.. currentmodule:: dataviz.classification.multilabel

.. autofunction:: label_cooccurrence_heatmap_static

Use case
--------

Use during EDA of multilabel targets to find label pairs that co-occur; supports raw counts or Jaccard normalization.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multilabel import label_cooccurrence_heatmap_static

   rng = np.random.default_rng(42)
   # symptom tags on clinic visits; "fever" and "cough" co-occur often
   n = 150
   labels = ["fever", "cough", "fatigue", "nausea", "rash"]
   base = rng.random((n, len(labels)))
   Y = (base < 0.25).astype(int)
   pair = rng.random(n) < 0.6
   Y[pair, 0] = 1
   Y[pair, 1] = 1

   ax = label_cooccurrence_heatmap_static(Y, labels=labels,
                                          title="Symptom tag co-occurrence (Jaccard)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multilabel/label_cooccurrence_heatmap_static.png" alt="label_cooccurrence_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
