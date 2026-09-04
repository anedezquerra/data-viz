dataviz.univariate.advanced.raincloud_plot_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: raincloud_plot_interactive

Use case
--------

Use to combine density, box plot, and raw points in one raincloud view showing shape, quartiles, and observations together.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.advanced import raincloud_plot_interactive

   # Resting heart rates recorded by a wellness study cohort
   rng = np.random.default_rng(42)
   heart_rate = pd.Series(
       np.round(rng.normal(loc=68.0, scale=7.5, size=55), 1),
       name="heart_rate_bpm",
   )

   fig = raincloud_plot_interactive(
       heart_rate,
       title="Resting Heart Rate Raincloud",
       ylabel="Heart Rate (bpm)",
       color="mediumpurple",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/raincloud_plot_interactive.png" alt="raincloud_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
