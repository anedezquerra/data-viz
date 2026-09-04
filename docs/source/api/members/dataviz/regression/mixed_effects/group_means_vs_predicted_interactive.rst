dataviz.regression.mixed_effects.group_means_vs_predicted_interactive
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.mixed_effects</p></div>

.. currentmodule:: dataviz.regression.mixed_effects

.. autofunction:: group_means_vs_predicted_interactive

Use case
--------

Use to compare observed group means against mixed-model predicted means to spot groups the model fits poorly.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.mixed_effects import group_means_vs_predicted_interactive

   rng = np.random.default_rng(42)
   lines = pd.Series([f"Line {c}" for c in "ABCDEFGHIJ"], name="line")
   observed = pd.Series(rng.normal(92.0, 4.0, size=10).round(2), name="observed_yield")
   predicted = pd.Series(observed + rng.normal(0.0, 1.5, size=10), name="predicted_yield")

   fig = group_means_vs_predicted_interactive(
       lines, observed, predicted,
       title="Manufacturing yield: observed vs mixed-model predicted",
       obs_color="#1b9e77", pred_color="#d95f02", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/mixed_effects/group_means_vs_predicted_interactive.png" alt="group_means_vs_predicted_interactive example output"><figcaption>Example output</figcaption></figure></div>
