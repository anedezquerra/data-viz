dataviz.classification.model_comparison.psi_bar_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: psi_bar_interactive

Use case
--------

Use to quantify population stability with per-bin PSI contributions and the total PSI against stability tiers.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.model_comparison import psi_bar_interactive

   rng = np.random.default_rng(83)
   scores_reference = np.clip(rng.beta(2, 4, 150), 0.01, 0.99)
   # seasonal campaign pushed noticeably higher-risk applicants into the funnel
   scores_current = np.clip(rng.beta(3.0, 3.4, 150), 0.01, 0.99)

   fig = psi_bar_interactive(
       scores_reference, scores_current, n_bins=8,
       title="Application risk score: PSI vs training baseline",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/psi_bar_interactive.png" alt="psi_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
