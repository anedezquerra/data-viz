dataviz.regression.effects.interaction_effect_plot_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: interaction_effect_plot_interactive

Use case
--------

Use to show how the effect of one feature changes across levels of a second feature, exposing interactions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.effects import interaction_effect_plot_interactive

   grid = np.linspace(20, 90, 20)
   curves = np.vstack([
       100 + 0.5 * grid,
       100 + 0.9 * grid + 0.01 * grid ** 2,
       100 + 1.4 * grid + 0.03 * grid ** 2,
   ])
   labels = ["low humidity", "medium humidity", "high humidity"]

   fig = interaction_effect_plot_interactive(
       grid, curves, labels,
       title="Interaction: Temperature x Humidity on Drying Time",
       feature_name="temperature (C)", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/interaction_effect_plot_interactive.png" alt="interaction_effect_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
