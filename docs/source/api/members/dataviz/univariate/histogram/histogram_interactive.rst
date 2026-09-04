dataviz.univariate.histogram.histogram_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.histogram</p></div>

.. currentmodule:: dataviz.univariate.histogram

.. autofunction:: histogram_interactive

Use case
--------

Use when profiling a numeric column for the first time with hoverable bin counts and zoomable ranges.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.histogram import histogram_interactive

   # Call-center wait times sampled during business hours
   rng = np.random.default_rng(42)
   wait_min = pd.Series(
       np.round(rng.gamma(shape=2.0, scale=2.5, size=60), 1),
       name="wait_time_min",
   )

   fig = histogram_interactive(
       wait_min,
       bins=14,
       title="Call-Center Wait Time Distribution",
       xlabel="Wait Time (min)",
       ylabel="Calls",
       marker_color="cornflowerblue",
       alpha=0.8,
       bargap=0.05,
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/histogram/histogram_interactive.png" alt="histogram_interactive example output"><figcaption>Example output</figcaption></figure></div>
