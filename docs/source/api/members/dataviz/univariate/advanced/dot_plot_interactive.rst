dataviz.univariate.advanced.dot_plot_interactive
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: dot_plot_interactive

Use case
--------

Use as a Cleveland dot plot to compare category counts with less ink than bars, emphasizing position over length.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.advanced import dot_plot_interactive

   # Support tickets classified by resolution channel last quarter
   rng = np.random.default_rng(42)
   channels = pd.Series(
       rng.choice(
           ["Email", "Phone", "Chat", "Self-Service", "Social", "In Person", "Forum"],
           size=320,
           p=[0.28, 0.24, 0.20, 0.12, 0.08, 0.05, 0.03],
       ),
       name="channel",
   )

   fig = dot_plot_interactive(
       channels,
       title="Tickets by Resolution Channel",
       xlabel="Tickets Resolved",
       ylabel="Channel",
       color="seagreen",
       top_n=6,
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/dot_plot_interactive.png" alt="dot_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
