dataviz.classification.fairness.per_segment_metric_bar_interactive
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.fairness</p></div>

.. currentmodule:: dataviz.classification.fairness

.. autofunction:: per_segment_metric_bar_interactive

Use case
--------

Use to audit accuracy, F1, TPR or FPR side by side across demographic or segment groups.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.fairness import per_segment_metric_bar_interactive

   rng = np.random.default_rng(47)
   n = 180
   groups = rng.choice(["urban", "suburban", "rural"], size=n, p=[0.45, 0.35, 0.2])
   base = {"urban": 0.55, "suburban": 0.50, "rural": 0.42}
   y_prob = np.array([base[g] for g in groups]) + rng.normal(0, 0.2, n)
   y_true = (rng.uniform(size=n) < np.clip(y_prob, 0.02, 0.98)).astype(int)
   y_pred = (y_prob >= 0.5).astype(int)

   fig = per_segment_metric_bar_interactive(
       y_true, y_pred, groups,
       metrics=("accuracy", "tpr", "fpr", "selection_rate"),
       title="Housing assistance model: metrics by region",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/fairness/per_segment_metric_bar_interactive.png" alt="per_segment_metric_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
