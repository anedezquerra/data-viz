dataviz.regression.bayesian.credible_interval_forest_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.bayesian</p></div>

.. currentmodule:: dataviz.regression.bayesian

.. autofunction:: credible_interval_forest_interactive

Use case
--------

Use to compare credible intervals across coefficients at a glance, seeing which effects are credibly different from zero.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.bayesian import credible_interval_forest_interactive

   names = ["ad_spend", "price_index", "seasonality", "distribution"]
   means = np.array([0.42, -1.15, 0.28, 0.66])
   lower = means - np.array([0.18, 0.30, 0.22, 0.25])
   upper = means + np.array([0.20, 0.28, 0.24, 0.27])

   fig = credible_interval_forest_interactive(
       names, means, lower, upper,
       title="Marketing Mix Model: 94% Credible Intervals",
       color="#2a7f62", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/bayesian/credible_interval_forest_interactive.png" alt="credible_interval_forest_interactive example output"><figcaption>Example output</figcaption></figure></div>
