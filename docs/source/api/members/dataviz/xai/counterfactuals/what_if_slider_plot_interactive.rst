dataviz.xai.counterfactuals.what_if_slider_plot_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.counterfactuals</p></div>

.. currentmodule:: dataviz.xai.counterfactuals

.. autofunction:: what_if_slider_plot_interactive

Use case
--------

Use to sweep one feature and watch the predicted outcome change, answering what-if questions for end users.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.counterfactuals import what_if_slider_plot_interactive

   grid = np.linspace(500, 800, 60)
   pred_default = 1.0 / (1.0 + np.exp((grid - 645.0) / 45.0))

   fig = what_if_slider_plot_interactive(
       grid,
       pred_default,
       feature_name="Credit score",
       current_value=612,
       threshold=0.5,
       title="What-If: Sweeping Credit Score for Applicant #417",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/counterfactuals/what_if_slider_plot_interactive.png" alt="what_if_slider_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
