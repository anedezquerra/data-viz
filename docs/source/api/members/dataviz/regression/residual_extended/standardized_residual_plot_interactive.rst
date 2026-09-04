dataviz.regression.residual_extended.standardized_residual_plot_interactive
===========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: standardized_residual_plot_interactive

Use case
--------

Use to flag outlying observations by plotting residuals scaled by their estimated standard deviation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.residual_extended import standardized_residual_plot_interactive

   rng = np.random.default_rng(42)
   claims = pd.Series(np.arange(1, 33), name="claim")
   actual_payout = pd.Series(
       rng.uniform(2, 95, 32).round(1), name="actual_payout_kusd"
   )
   predicted_payout = pd.Series(
       actual_payout + rng.normal(0, 5, 32), name="predicted_payout_kusd"
   )
   predicted_payout.iloc[7] -= 28  # flagged outlier claim

   fig = standardized_residual_plot_interactive(
       actual_payout, predicted_payout, bound=2.0,
       title="Insurance payout model: standardized residuals",
       color="#ee854a", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/standardized_residual_plot_interactive.png" alt="standardized_residual_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
