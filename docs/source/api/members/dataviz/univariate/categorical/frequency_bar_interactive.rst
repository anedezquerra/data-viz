dataviz.univariate.categorical.frequency_bar_interactive
========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.categorical</p></div>

.. currentmodule:: dataviz.univariate.categorical

.. autofunction:: frequency_bar_interactive

Use case
--------

Use to show how often each category occurs with hover labels, with normalize=True when proportions matter more than raw counts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.categorical import frequency_bar_interactive

   # Exit-survey responses for a public library membership program
   rng = np.random.default_rng(42)
   ratings = pd.Series(
       rng.choice(
           ["Excellent", "Good", "Average", "Poor"],
           size=180,
           p=[0.45, 0.32, 0.16, 0.07],
       ),
       name="rating",
   )

   fig = frequency_bar_interactive(
       ratings,
       normalize=True,
       title="Library Exit Survey Ratings",
       xlabel="Rating",
       ylabel="Proportion of Responses",
       color="slateblue",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/categorical/frequency_bar_interactive.png" alt="frequency_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
