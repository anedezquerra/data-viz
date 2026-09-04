dataviz.spc.variable.median_chart_interactive
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.variable</p></div>

.. currentmodule:: dataviz.spc.variable

.. autofunction:: median_chart_interactive

Use case
--------

Use when monitoring subgrouped measurements by subgroup median, a robust X-tilde alternative when outliers skew the mean.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.variable import median_chart_interactive

   rng = np.random.default_rng(42)
   # Hardness readings (HRC): 24 subgroups of 5 parts from heat treatment
   hardness = rng.normal(58.0, 1.2, size=120)
   hardness[75:80] -= 3.5  # quench-tank temperature drop in subgroup 15

   fig = median_chart_interactive(hardness, subgroup_size=5, title="Part Hardness Median Chart")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/variable/median_chart_interactive.png" alt="median_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
