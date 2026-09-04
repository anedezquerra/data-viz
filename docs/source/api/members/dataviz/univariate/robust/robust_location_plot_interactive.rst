dataviz.univariate.robust.robust_location_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.robust</p></div>

.. currentmodule:: dataviz.univariate.robust

.. autofunction:: robust_location_plot_interactive

Use case
--------

Use to see where the median, trimmed mean, and winsorized mean fall on the histogram and spot disagreement between centers.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.robust import robust_location_plot_interactive

   rng = np.random.default_rng(42)
   income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
   income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
   household_income = pd.Series(income_k, name="household_income_k")
   fig = robust_location_plot_interactive(
       household_income,
       title="Household Income with Robust Location Estimates",
       color="lightsteelblue",
       height=500,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/robust/robust_location_plot_interactive.png" alt="robust_location_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
