dataviz.classification.threshold_extra.f_beta_curve_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold_extra</p></div>

.. currentmodule:: dataviz.classification.threshold_extra

.. autofunction:: f_beta_curve_interactive

Use case
--------

Use when recall matters more or less than precision; sweeps F-beta for several beta values across thresholds.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold_extra import f_beta_curve_interactive

   rng = np.random.default_rng(42)
   # defect detector: recall-weighted (F2) vs precision-weighted (F0.5) views
   n = 150
   y_true = (rng.random(n) < 0.3).astype(int)
   y_prob = np.clip(
       y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

   fig = f_beta_curve_interactive(y_true, y_prob, betas=(0.5, 1.0, 2.0),
                                  title="Defect detector: F-beta vs threshold")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold_extra/f_beta_curve_interactive.png" alt="f_beta_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
