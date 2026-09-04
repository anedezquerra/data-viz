dataviz.bivariate.categorical.grouped_bar_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.categorical</p></div>

.. currentmodule:: dataviz.bivariate.categorical

.. autofunction:: grouped_bar_interactive

Use case
--------

Use to compare an aggregated numeric value, such as a mean or sum, across the levels of a categorical variable.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.categorical import grouped_bar_interactive

   rng = np.random.default_rng(42)
   n = 90
   region = pd.Series(np.repeat(["North", "South", "East", "West"], n // 4)[:n], name="Region")
   sales = pd.Series(rng.normal(loc=120.0, scale=25.0, size=n), name="Quarterly sales (k USD)")

   fig = grouped_bar_interactive(
       region,
       sales,
       aggfunc="median",
       title="Median Quarterly Sales by Region",
       color="seagreen",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/categorical/grouped_bar_interactive.png" alt="grouped_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
