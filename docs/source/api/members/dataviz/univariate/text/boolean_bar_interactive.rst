dataviz.univariate.text.boolean_bar_interactive
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.text</p></div>

.. currentmodule:: dataviz.univariate.text

.. autofunction:: boolean_bar_interactive

Use case
--------

Use to plot true/false counts for a binary indicator as a semantic wrapper around categorical frequency bars.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.text import boolean_bar_interactive

   rng = np.random.default_rng(42)
   subscribed = pd.Series(rng.random(120) < 0.42, name="newsletter_subscribed")
   fig = boolean_bar_interactive(
       subscribed,
       title="Newsletter Subscription Status",
       color="seagreen",
       height=450,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/text/boolean_bar_interactive.png" alt="boolean_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
