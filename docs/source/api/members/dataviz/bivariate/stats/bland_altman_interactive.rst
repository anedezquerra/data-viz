dataviz.bivariate.stats.bland_altman_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autofunction:: bland_altman_interactive

Use case
--------

Use when comparing two measurement methods to assess their agreement and bias rather than their correlation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.stats import bland_altman_interactive

   rng = np.random.default_rng(42)
   n = 60
   lab_test = pd.Series(rng.normal(loc=120.0, scale=18.0, size=n), name="Lab assay (mg/dL)")
   home_test = pd.Series(lab_test + rng.normal(loc=2.0, scale=6.0, size=n), name="Home kit (mg/dL)")

   fig = bland_altman_interactive(
       lab_test,
       home_test,
       title="Bland-Altman: Lab vs Home Kit",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/stats/bland_altman_interactive.png" alt="bland_altman_interactive example output"><figcaption>Example output</figcaption></figure></div>
