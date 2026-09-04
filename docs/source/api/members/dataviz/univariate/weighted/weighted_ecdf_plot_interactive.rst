dataviz.univariate.weighted.weighted_ecdf_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.weighted</p></div>

.. currentmodule:: dataviz.univariate.weighted

.. autofunction:: weighted_ecdf_plot_interactive

Use case
--------

Use to plot the empirical cumulative distribution when observations contribute unequal weight.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.weighted import weighted_ecdf_plot_interactive

   rng = np.random.default_rng(42)
   nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
   sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
   fig = weighted_ecdf_plot_interactive(
       nps_score,
       sample_weight,
       title="Weighted ECDF of NPS Scores",
       color="indigo",
       height=500,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/weighted/weighted_ecdf_plot_interactive.png" alt="weighted_ecdf_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
