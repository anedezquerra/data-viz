dataviz.classification.errors.discrimination_threshold_dashboard_interactive
============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.errors</p></div>

.. currentmodule:: dataviz.classification.errors

.. autofunction:: discrimination_threshold_dashboard_interactive

Use case
--------

Use to pick an operating threshold by viewing precision, recall, F1 and queue rate together across all thresholds.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.errors import (
       discrimination_threshold_dashboard_interactive,
   )

   rng = np.random.default_rng(37)
   n_pos, n_neg = 45, 115
   y_true = np.concatenate([np.ones(n_pos, int), np.zeros(n_neg, int)])
   y_prob = np.concatenate([
       rng.normal(0.66, 0.16, n_pos),
       rng.normal(0.34, 0.16, n_neg),
   ]).clip(0.01, 0.99)

   fig = discrimination_threshold_dashboard_interactive(
       y_true, y_prob, n_thresholds=80,
       title="Churn outreach: picking the operating threshold",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/errors/discrimination_threshold_dashboard_interactive.png" alt="discrimination_threshold_dashboard_interactive example output"><figcaption>Example output</figcaption></figure></div>
