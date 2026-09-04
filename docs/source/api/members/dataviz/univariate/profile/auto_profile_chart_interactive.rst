dataviz.univariate.profile.auto_profile_chart_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.profile</p></div>

.. currentmodule:: dataviz.univariate.profile

.. autofunction:: auto_profile_chart_interactive

Use case
--------

Use when you want one sensible interactive chart chosen automatically from the inferred variable type.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.profile import auto_profile_chart_interactive

   rng = np.random.default_rng(42)
   customers = pd.DataFrame(
       {"monthly_spend": rng.gamma(shape=3.0, scale=28.0, size=150).round(2)}
   )
   customers.loc[[5, 41, 96], "monthly_spend"] = np.nan
   fig = auto_profile_chart_interactive(
       "monthly_spend",
       data=customers,
       title="Monthly Spend Profile",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/profile/auto_profile_chart_interactive.png" alt="auto_profile_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
