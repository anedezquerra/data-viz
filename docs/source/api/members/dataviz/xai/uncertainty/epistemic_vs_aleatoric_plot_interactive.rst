dataviz.xai.uncertainty.epistemic_vs_aleatoric_plot_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: epistemic_vs_aleatoric_plot_interactive

Use case
--------

Use to decompose uncertainty into reducible epistemic (model) and irreducible aleatoric (data) components across bins.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.uncertainty import epistemic_vs_aleatoric_plot_interactive

   bin_centers = np.linspace(0.0, 1.0, 20)
   epistemic = 0.05 + 0.12 * (bin_centers - 0.5) ** 2 * 4
   aleatoric = 0.08 + 0.05 * np.sin(np.pi * bin_centers)
   fig = epistemic_vs_aleatoric_plot_interactive(
       bin_centers, epistemic, aleatoric,
       title="Uncertainty decomposition across predicted-risk deciles",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/uncertainty/epistemic_vs_aleatoric_plot_interactive.png" alt="epistemic_vs_aleatoric_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
