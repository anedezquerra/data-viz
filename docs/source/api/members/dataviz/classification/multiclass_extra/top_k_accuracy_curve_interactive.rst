dataviz.classification.multiclass_extra.top_k_accuracy_curve_interactive
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass_extra</p></div>

.. currentmodule:: dataviz.classification.multiclass_extra

.. autofunction:: top_k_accuracy_curve_interactive

Use case
--------

Use when predictions feed a downstream re-ranker; shows how accuracy grows as the top-K candidate set widens.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass_extra import top_k_accuracy_curve_interactive

   rng = np.random.default_rng(42)
   # 6-class product recommender: does the right item appear in the top-K?
   n = 120
   n_classes = 6
   y_true = rng.integers(0, n_classes, n)
   logits = rng.normal(0, 1, (n, n_classes))
   logits[np.arange(n), y_true] += 2.2  # model signal on the true class
   probs = np.exp(logits) / np.exp(logits).sum(axis=1, keepdims=True)

   fig = top_k_accuracy_curve_interactive(y_true, probs,
                                          title="Recommender top-K accuracy")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass_extra/top_k_accuracy_curve_interactive.png" alt="top_k_accuracy_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
