dataviz.classification.calibration_extra.platt_isotonic_overlay_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: platt_isotonic_overlay_interactive

Use case
--------

Use when choosing a recalibration method by comparing raw, Platt-scaled and isotonic mappings against binned observations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.calibration_extra import (
       platt_isotonic_overlay_interactive,
   )

   rng = np.random.default_rng(5)
   n = 150
   signal = rng.normal(0, 1.5, n)
   y_true = (signal + rng.normal(0, 0.8, n) > 0).astype(int)
   y_prob = 1.0 / (1.0 + np.exp(-2.5 * signal))  # over-confident raw scores
   y_prob = np.clip(y_prob, 1e-4, 1 - 1e-4)

   fig = platt_isotonic_overlay_interactive(
       y_true, y_prob, n_bins=10,
       title="SVM spam filter: Platt vs isotonic recalibration",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration_extra/platt_isotonic_overlay_interactive.png" alt="platt_isotonic_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
