dataviz.classification.threshold_extra.youden_j_curve_interactive
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold_extra</p></div>

.. currentmodule:: dataviz.classification.threshold_extra

.. autofunction:: youden_j_curve_interactive

Use case
--------

Use to find the threshold maximizing sensitivity plus specificity; plots both components and Youden's J.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold_extra import youden_j_curve_interactive

   rng = np.random.default_rng(42)
   # screening assay: choose the cut-off maximising Youden's J
   n = 150
   y_true = (rng.random(n) < 0.3).astype(int)
   y_prob = np.clip(
       y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

   fig = youden_j_curve_interactive(y_true, y_prob,
                                    title="Screening assay: Youden's J")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold_extra/youden_j_curve_interactive.png" alt="youden_j_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
