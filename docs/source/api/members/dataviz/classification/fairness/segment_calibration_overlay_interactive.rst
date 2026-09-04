dataviz.classification.fairness.segment_calibration_overlay_interactive
=======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.fairness</p></div>

.. currentmodule:: dataviz.classification.fairness

.. autofunction:: segment_calibration_overlay_interactive

Use case
--------

Use to check whether probability calibration holds equally well across subgroups.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.fairness import (
       segment_calibration_overlay_interactive,
   )

   rng = np.random.default_rng(61)
   n = 180
   groups = rng.choice(["app", "web", "branch"], size=n, p=[0.5, 0.3, 0.2])
   y_prob = np.clip(rng.beta(2, 3, n), 0.01, 0.99)
   bias = {"app": 0.0, "web": 0.05, "branch": -0.07}
   y_true = (rng.uniform(size=n)
             < np.clip(y_prob + np.array([bias[g] for g in groups]), 0, 1)
             ).astype(int)

   fig = segment_calibration_overlay_interactive(
       y_true, y_prob, groups, n_bins=6,
       title="Loan approval model: calibration by application channel",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/fairness/segment_calibration_overlay_interactive.png" alt="segment_calibration_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
