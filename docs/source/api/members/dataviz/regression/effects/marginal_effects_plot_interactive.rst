dataviz.regression.effects.marginal_effects_plot_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: marginal_effects_plot_interactive

Use case
--------

Use to report average marginal effect per feature with optional confidence intervals, e.g. for econometric model interpretation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.effects import marginal_effects_plot_interactive

   features = ["discount_pct", "shelf_position", "weekend", "ad_impressions_k"]
   effects = np.array([1.9, 0.7, 0.4, 0.15])
   lo = effects - np.array([0.4, 0.3, 0.35, 0.2])
   hi = effects + np.array([0.45, 0.3, 0.35, 0.22])

   fig = marginal_effects_plot_interactive(
       features, effects, ci_lower=lo, ci_upper=hi,
       title="Promo Response Model: Average Marginal Effects",
       color="#2a7f62", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/marginal_effects_plot_interactive.png" alt="marginal_effects_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
