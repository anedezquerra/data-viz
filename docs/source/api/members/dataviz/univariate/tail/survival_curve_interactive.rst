dataviz.univariate.tail.survival_curve_interactive
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.tail</p></div>

.. currentmodule:: dataviz.univariate.tail

.. autofunction:: survival_curve_interactive

Use case
--------

Use to emphasize upper-tail behavior by plotting the probability of exceeding each value instead of a density.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.tail import survival_curve_interactive

   rng = np.random.default_rng(42)
   claim_amounts = pd.Series(
       (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
       name="claim_amount",
   )
   fig = survival_curve_interactive(
       claim_amounts,
       title="Insurance Claim Survival Curve",
       color="darkred",
       height=500,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/tail/survival_curve_interactive.png" alt="survival_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
