dataviz.classification.confusion_extended.normalized_confusion_matrix_interactive
=================================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.confusion_extended</p></div>

.. currentmodule:: dataviz.classification.confusion_extended

.. autofunction:: normalized_confusion_matrix_interactive

Use case
--------

Use instead of raw counts when classes are imbalanced; normalize by true, pred or all to read recall or precision per class.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.confusion_extended import (
       normalized_confusion_matrix_interactive,
   )

   rng = np.random.default_rng(8)
   n = 180
   true_labels = rng.choice(3, size=n, p=[0.5, 0.3, 0.2])
   pred_labels = true_labels.copy()
   flip = rng.uniform(size=n) < 0.15
   pred_labels[flip] = rng.choice(3, size=int(flip.sum()))
   cm = np.zeros((3, 3), dtype=int)
   for t, p in zip(true_labels, pred_labels):
       cm[t, p] += 1
   classes = ["low", "medium", "high"]

   fig = normalized_confusion_matrix_interactive(
       cm, labels=classes, normalize="true",
       title="Support ticket priority: per-class recall matrix",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/confusion_extended/normalized_confusion_matrix_interactive.png" alt="normalized_confusion_matrix_interactive example output"><figcaption>Example output</figcaption></figure></div>
