dataviz.regression.coefficients.coefficient_path_plot_interactive
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.coefficients</p></div>

.. currentmodule:: dataviz.regression.coefficients

.. autofunction:: coefficient_path_plot_interactive

Use case
--------

Use to trace coefficient paths across a regularization parameter and see which features shrink out first in ridge or lasso fits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.coefficients import coefficient_path_plot_interactive

   alphas = np.logspace(-3, 1, 20)
   features = ["income", "debt_ratio", "credit_age", "utilization"]
   true_betas = np.array([0.9, -1.4, 0.5, -0.8])
   paths = true_betas[None, :] * (1 - np.exp(-alphas[:, None] * 5))

   fig = coefficient_path_plot_interactive(alphas, paths, feature_names=features,
                                           log_x=True,
                                           title="Credit Risk Lasso: Coefficient Path",
                                           template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/coefficients/coefficient_path_plot_interactive.png" alt="coefficient_path_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
