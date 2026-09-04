dataviz.bivariate.categorical.crosstab_heatmap_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: crosstab_heatmap_interactive

Use case
--------

Use to spot associations between two categorical variables by mapping their contingency table to color intensity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.categorical import crosstab_heatmap_interactive

   rng = np.random.default_rng(42)
   n = 200
   channel = pd.Series(rng.choice(["Email", "Social", "Search", "Referral"], size=n), name="Channel")
   converted = pd.Series(rng.choice(["Converted", "Bounced"], size=n, p=[0.35, 0.65]), name="Outcome")

   fig = crosstab_heatmap_interactive(
       channel,
       converted,
       normalize="index",
       title="Conversion Rate by Channel",
       colorscale="YlGn",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/crosstab_heatmap_interactive.png" alt="crosstab_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
