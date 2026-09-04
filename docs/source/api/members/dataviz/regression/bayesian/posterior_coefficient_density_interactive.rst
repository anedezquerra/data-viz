dataviz.regression.bayesian.posterior_coefficient_density_interactive
=====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.bayesian</p></div>

.. currentmodule:: dataviz.regression.bayesian

.. autofunction:: posterior_coefficient_density_interactive

Use case
--------

Use to inspect the full posterior distribution of each coefficient from MCMC samples instead of relying on a single point estimate.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.bayesian import posterior_coefficient_density_interactive

   rng = np.random.default_rng(42)
   samples = [rng.normal(2.1, 0.4, 600),
              rng.normal(-0.7, 0.25, 600),
              rng.normal(0.05, 0.5, 600),
              rng.normal(1.3, 0.3, 600)]
   names = ["sqft", "bedrooms", "age_years", "dist_transit_km"]

   fig = posterior_coefficient_density_interactive(
       samples, coef_names=names,
       title="Hedonic Pricing Model: Posterior Coefficient Densities",
       template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/bayesian/posterior_coefficient_density_interactive.png" alt="posterior_coefficient_density_interactive example output"><figcaption>Example output</figcaption></figure></div>
