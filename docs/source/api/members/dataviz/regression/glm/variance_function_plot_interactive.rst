dataviz.regression.glm.variance_function_plot_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.glm</p></div>

.. currentmodule:: dataviz.regression.glm

.. autofunction:: variance_function_plot_interactive

Use case
--------

Use to visualize the mean-variance relationship V(mu) implied by the chosen GLM family.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.glm import variance_function_plot_interactive

   rng = np.random.default_rng(42)
   mu_grid = pd.Series(np.exp(np.linspace(np.log(0.5), np.log(25.0), 30)),
                       name="mean_defect_count")

   fig = variance_function_plot_interactive(
       mu_grid, family="poisson",
       title="Defect Count Model: Poisson Variance Function",
       template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/glm/variance_function_plot_interactive.png" alt="variance_function_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
