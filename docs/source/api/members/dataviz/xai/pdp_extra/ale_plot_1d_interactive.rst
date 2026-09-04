dataviz.xai.pdp_extra.ale_plot_1d_interactive
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.pdp_extra</p></div>

.. currentmodule:: dataviz.xai.pdp_extra

.. autofunction:: ale_plot_1d_interactive

Use case
--------

Use instead of PDP when features are correlated; ALE accumulates local effects within data-supported bins to avoid extrapolation bias.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.pdp_extra import ale_plot_1d_interactive

   bin_edges = np.linspace(0.0, 0.6, 11)
   centers = (bin_edges[:-1] + bin_edges[1:]) / 2
   ale = 2.1 * centers - 0.9 * centers ** 2
   ale = ale - ale.mean()
   fig = ale_plot_1d_interactive(
       bin_edges, ale, feature_name="debt_to_income",
       title="ALE of debt-to-income on default log-odds",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/pdp_extra/ale_plot_1d_interactive.png" alt="ale_plot_1d_interactive example output"><figcaption>Example output</figcaption></figure></div>
