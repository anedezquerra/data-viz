dataviz.classification.multilabel.multilabel_confusion_grid_interactive
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multilabel</p></div>

.. currentmodule:: dataviz.classification.multilabel

.. autofunction:: multilabel_confusion_grid_interactive

Use case
--------

Use to audit a multilabel model label by label; small-multiples grid holds one 2x2 confusion matrix per label.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multilabel import multilabel_confusion_grid_interactive

   rng = np.random.default_rng(42)
   # multilabel movie-tagging model: 5 genre tags, 120 movies
   n, n_labels = 120, 5
   labels = ["action", "comedy", "drama", "romance", "scifi"]
   Y_true = (rng.random((n, n_labels)) < 0.3).astype(int)
   noise = rng.random((n, n_labels)) < 0.12
   Y_pred = np.where(noise, 1 - Y_true, Y_true)

   fig = multilabel_confusion_grid_interactive(Y_true, Y_pred, labels=labels,
                                               title="Movie tagger: per-tag matrices")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multilabel/multilabel_confusion_grid_interactive.png" alt="multilabel_confusion_grid_interactive example output"><figcaption>Example output</figcaption></figure></div>
