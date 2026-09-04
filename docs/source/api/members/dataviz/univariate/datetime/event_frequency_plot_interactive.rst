dataviz.univariate.datetime.event_frequency_plot_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.datetime</p></div>

.. currentmodule:: dataviz.univariate.datetime

.. autofunction:: event_frequency_plot_interactive

Use case
--------

Use to chart how event counts evolve over time from raw datetime observations at a chosen frequency.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.datetime import event_frequency_plot_interactive

   # Newsletter signup timestamps exported from a marketing platform
   rng = np.random.default_rng(42)
   signups = pd.Series(
       pd.Timestamp("2026-01-05")
       + pd.to_timedelta(rng.uniform(0, 90 * 24, size=40), unit="h"),
       name="signup_time",
   )

   fig = event_frequency_plot_interactive(
       signups,
       freq="W",
       title="Weekly Newsletter Signups",
       xlabel="Week",
       ylabel="Signups",
       color="darkcyan",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/datetime/event_frequency_plot_interactive.png" alt="event_frequency_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
