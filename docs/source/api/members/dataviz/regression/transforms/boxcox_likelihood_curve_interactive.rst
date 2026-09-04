dataviz.regression.transforms.boxcox_likelihood_curve_interactive
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.transforms</p></div>

.. currentmodule:: dataviz.regression.transforms

.. autofunction:: boxcox_likelihood_curve_interactive

Use case
--------

Use to choose a Box-Cox power for the response by reading the profile log-likelihood over lambda and its maximizer.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.transforms import boxcox_likelihood_curve_interactive

   rng = np.random.default_rng(42)
   claim_amount = rng.gamma(shape=2.0, scale=1800.0, size=60)  # right-skewed, > 0

   fig = boxcox_likelihood_curve_interactive(
       claim_amount, lambdas=np.linspace(-1.5, 1.5, 91),
       title="Auto insurance claims: Box-Cox profile log-likelihood",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/transforms/boxcox_likelihood_curve_interactive.png" alt="boxcox_likelihood_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
