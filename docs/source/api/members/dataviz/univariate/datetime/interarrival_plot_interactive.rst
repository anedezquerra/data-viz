dataviz.univariate.datetime.interarrival_plot_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.datetime</p></div>

.. currentmodule:: dataviz.univariate.datetime

.. autofunction:: interarrival_plot_interactive

Use case
--------

Use to histogram the gaps between consecutive events to spot burstiness or regularity in timing.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.datetime import interarrival_plot_interactive

   # Equipment failure timestamps from a fleet monitoring system
   rng = np.random.default_rng(42)
   failures = pd.Series(
       pd.Timestamp("2026-02-01")
       + pd.to_timedelta(np.sort(rng.uniform(0, 120 * 24, size=32)), unit="h"),
       name="failure_time",
   )

   fig = interarrival_plot_interactive(
       failures,
       unit="h",
       title="Time Between Equipment Failures",
       color="indianred",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/datetime/interarrival_plot_interactive.png" alt="interarrival_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
