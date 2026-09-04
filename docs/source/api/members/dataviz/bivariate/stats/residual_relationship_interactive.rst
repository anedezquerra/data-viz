dataviz.bivariate.stats.residual_relationship_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: residual_relationship_interactive

Use case
--------

Use to check whether a polynomial fit leaves structure in the residuals, signaling a poor model choice.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.stats import residual_relationship_interactive

   rng = np.random.default_rng(42)
   n = 70
   experience = pd.Series(rng.uniform(low=0.0, high=20.0, size=n), name="Experience (years)")
   salary = pd.Series(40.0 + 4.0 * experience + 0.08 * experience**2 + rng.normal(loc=0.0, scale=6.0, size=n), name="Salary (k USD)")

   fig = residual_relationship_interactive(
       experience,
       salary,
       degree=1,
       title="Linear Fit Residuals: Salary vs Experience",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/residual_relationship_interactive.png" alt="residual_relationship_interactive example output"><figcaption>Example output</figcaption></figure></div>
