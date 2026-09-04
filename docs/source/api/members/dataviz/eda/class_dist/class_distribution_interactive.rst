dataviz.eda.class_dist.class_distribution_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.eda.class_dist</p></div>

.. currentmodule:: dataviz.eda.class_dist

.. autofunction:: class_distribution_interactive

Use case
--------

Use to check target class balance before training a classifier and decide whether rebalancing is needed.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.eda.class_dist import class_distribution_interactive

   rng = np.random.default_rng(42)
   tickets = pd.Series(
       rng.choice(["Low", "Medium", "High", "Critical"], size=150, p=[0.45, 0.3, 0.18, 0.07]),
       name="Ticket priority",
   )

   fig = class_distribution_interactive(
       tickets,
       title="Support Ticket Priority Balance",
       color="steelblue",
       sort=True,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/eda/class_dist/class_distribution_interactive.png" alt="class_distribution_interactive example output"><figcaption>Example output</figcaption></figure></div>
