dataviz.univariate.categorical.pareto_chart_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.categorical</p></div>

.. currentmodule:: dataviz.univariate.categorical

.. autofunction:: pareto_chart_interactive

Use case
--------

Use to rank categories by frequency with a cumulative percentage line, highlighting the vital few that drive most cases.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.categorical import pareto_chart_interactive

   # Assembly-line defect codes logged during a quality audit
   rng = np.random.default_rng(42)
   defects = pd.Series(
       rng.choice(
           ["Scratch", "Misalignment", "Dent", "Paint Void", "Loose Fastener", "Label Error"],
           size=260,
           p=[0.34, 0.26, 0.16, 0.11, 0.08, 0.05],
       ),
       name="defect_code",
   )

   fig = pareto_chart_interactive(
       defects,
       top_n=6,
       title="Pareto Chart of Assembly Defects",
       xlabel="Defect Code",
       ylabel="Occurrences",
       color="steelblue",
       line_color="firebrick",
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/categorical/pareto_chart_interactive.png" alt="pareto_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
