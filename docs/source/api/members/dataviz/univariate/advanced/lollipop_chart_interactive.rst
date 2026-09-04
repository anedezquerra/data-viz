dataviz.univariate.advanced.lollipop_chart_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.advanced</p></div>

.. currentmodule:: dataviz.univariate.advanced

.. autofunction:: lollipop_chart_interactive

Use case
--------

Use to compare category counts with stems and markers when bars feel too heavy for a slim ranking view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.advanced import lollipop_chart_interactive

   # Online orders grouped by product category for one month
   rng = np.random.default_rng(42)
   categories = pd.Series(
       rng.choice(
           ["Books", "Electronics", "Clothing", "Home", "Toys", "Sports", "Beauty"],
           size=280,
           p=[0.24, 0.22, 0.18, 0.14, 0.10, 0.07, 0.05],
       ),
       name="category",
   )

   fig = lollipop_chart_interactive(
       categories,
       title="Monthly Orders by Product Category",
       xlabel="Product Category",
       ylabel="Orders",
       color="navy",
       top_n=7,
       template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/advanced/lollipop_chart_interactive.png" alt="lollipop_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
