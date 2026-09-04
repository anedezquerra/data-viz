dataviz.classification.calibration_extra.sharpness_resolution_decomposition_interactive
=======================================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.calibration_extra</p></div>

.. currentmodule:: dataviz.classification.calibration_extra

.. autofunction:: sharpness_resolution_decomposition_interactive

Use case
--------

Use to decompose the Brier score into reliability, resolution and uncertainty to see why probability quality is poor.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.calibration_extra import (
       sharpness_resolution_decomposition_interactive,
   )

   rng = np.random.default_rng(9)
   n = 160
   y_prob = np.clip(rng.beta(2.5, 2.5, n), 0.01, 0.99)
   y_true = (rng.uniform(size=n) < y_prob).astype(int)

   fig = sharpness_resolution_decomposition_interactive(
       y_true, y_prob, n_bins=8,
       title="Readmission risk model: Murphy decomposition of Brier score",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/calibration_extra/sharpness_resolution_decomposition_interactive.png" alt="sharpness_resolution_decomposition_interactive example output"><figcaption>Example output</figcaption></figure></div>
