dataviz.bivariate.joint.bivariate_histogram_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.joint</p></div>

.. currentmodule:: dataviz.bivariate.joint

.. autofunction:: bivariate_histogram_interactive

Use case
--------

Use to summarize the joint distribution of two variables as rectangular bins when points overplot.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.joint import bivariate_histogram_interactive

   rng = np.random.default_rng(42)
   n = 600
   wait_min = pd.Series(rng.gamma(shape=3.0, scale=2.0, size=n), name="Wait time (min)")
   bill = pd.Series(15.0 + 2.0 * wait_min + rng.normal(loc=0.0, scale=8.0, size=n), name="Bill (USD)")

   fig = bivariate_histogram_interactive(
       wait_min,
       bill,
       nbinsx=25,
       nbinsy=25,
       title="Wait Time vs Bill Density",
       colorscale="Viridis",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/joint/bivariate_histogram_interactive.png" alt="bivariate_histogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
