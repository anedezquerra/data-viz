dataviz.univariate.density.density_interactive
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.density</p></div>

.. currentmodule:: dataviz.univariate.density

.. autofunction:: density_interactive

Use case
--------

Use to estimate the smooth probability density of a numeric variable with hover inspection of the curve.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.density import density_interactive

   # Nightly server room temperatures sampled by an IoT sensor
   rng = np.random.default_rng(42)
   temp_c = pd.Series(
       np.round(rng.normal(loc=21.5, scale=1.2, size=60), 2),
       name="temperature_c",
   )

   fig = density_interactive(
       temp_c,
       title="Server Room Temperature Density",
       xlabel="Temperature (C)",
       color="darkred",
       histnorm="probability density",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/density/density_interactive.png" alt="density_interactive example output"><figcaption>Example output</figcaption></figure></div>
