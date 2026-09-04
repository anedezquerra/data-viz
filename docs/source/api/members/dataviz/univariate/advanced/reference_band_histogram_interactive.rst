dataviz.univariate.advanced.reference_band_histogram_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: reference_band_histogram_interactive

Use case
--------

Use when you need a histogram annotated with mean and standard-deviation bands to judge spread against typical reference ranges.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.advanced import reference_band_histogram_interactive

   # Bottling line fill volumes audited over one production shift
   rng = np.random.default_rng(42)
   fill_ml = pd.Series(
       np.round(rng.normal(loc=500.0, scale=4.5, size=48), 1),
       name="fill_volume_ml",
   )

   fig = reference_band_histogram_interactive(
       fill_ml,
       bins=14,
       title="Bottle Fill Volume with +/- 1 SD Band",
       xlabel="Fill Volume (ml)",
       color="cornflowerblue",
       band_color="khaki",
       mean_color="crimson",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/reference_band_histogram_interactive.png" alt="reference_band_histogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
