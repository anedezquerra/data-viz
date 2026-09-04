dataviz.univariate.ordinal.ordinal_bar_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.ordinal</p></div>

.. currentmodule:: dataviz.univariate.ordinal

.. autofunction:: ordinal_bar_interactive

Use case
--------

Use to plot ordinal category counts or proportions in a fixed meaningful order, avoiding misleading frequency sorting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.ordinal import ordinal_bar_interactive

   rng = np.random.default_rng(42)
   scale = ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
   satisfaction = pd.Series(
       rng.choice(scale, size=220, p=[0.08, 0.17, 0.20, 0.35, 0.20]),
       name="satisfaction",
   )
   fig = ordinal_bar_interactive(
       satisfaction,
       order=scale,
       normalize=True,
       title="Post-Purchase Satisfaction Survey (n=220)",
       color="teal",
       height=500,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/ordinal/ordinal_bar_interactive.png" alt="ordinal_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
