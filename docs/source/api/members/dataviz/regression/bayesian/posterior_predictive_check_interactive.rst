dataviz.regression.bayesian.posterior_predictive_check_interactive
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.bayesian</p></div>

.. currentmodule:: dataviz.regression.bayesian

.. autofunction:: posterior_predictive_check_interactive

Use case
--------

Use to compare posterior-predictive draws against observed y and confirm the fitted Bayesian model can reproduce the data it was trained on.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.bayesian import posterior_predictive_check_interactive

   rng = np.random.default_rng(42)
   recovery = pd.Series(rng.normal(14.0, 3.0, 40), name="recovery_days")
   draws = recovery.to_numpy()[None, :] + rng.normal(0, 1.2, (40, 40))

   fig = posterior_predictive_check_interactive(
       recovery, draws,
       title="Clinical Trial: Posterior Predictive Check (Recovery Days)",
       true_color="#c0392b", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/bayesian/posterior_predictive_check_interactive.png" alt="posterior_predictive_check_interactive example output"><figcaption>Example output</figcaption></figure></div>
