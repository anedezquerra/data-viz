dataviz.classification.fairness.fairness_disparity_heatmap_interactive
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.fairness</p></div>

.. currentmodule:: dataviz.classification.fairness

.. autofunction:: fairness_disparity_heatmap_interactive

Use case
--------

Use to spot which groups deviate from the population mean on fairness metrics such as TPR or selection rate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.fairness import fairness_disparity_heatmap_interactive

   rng = np.random.default_rng(53)
   n = 180
   groups = rng.choice(["group A", "group B", "group C"], size=n,
                       p=[0.5, 0.3, 0.2])
   shift = {"group A": 0.08, "group B": 0.0, "group C": -0.10}
   y_prob = np.clip(0.5 + np.array([shift[g] for g in groups])
                    + rng.normal(0, 0.22, n), 0.02, 0.98)
   y_true = (rng.uniform(size=n) < y_prob).astype(int)
   y_pred = (y_prob >= 0.5).astype(int)

   fig = fairness_disparity_heatmap_interactive(
       y_true, y_pred, groups,
       title="Hiring screen: deviation from population mean per group",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/fairness/fairness_disparity_heatmap_interactive.png" alt="fairness_disparity_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
