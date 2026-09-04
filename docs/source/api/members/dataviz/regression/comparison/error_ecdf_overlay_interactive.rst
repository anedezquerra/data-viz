dataviz.regression.comparison.error_ecdf_overlay_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.comparison</p></div>

.. currentmodule:: dataviz.regression.comparison

.. autofunction:: error_ecdf_overlay_interactive

Use case
--------

Compare empirical CDFs of absolute error per model; the curve farthest up and left dominates on typical error magnitude.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.comparison import error_ecdf_overlay_interactive

   rng = np.random.default_rng(42)
   errors = [rng.normal(0, 4, 35),
             rng.normal(0, 7, 35),
             rng.normal(2, 10, 35)]
   labels = ["OLS", "Huber", "Quantile (median)"]

   fig = error_ecdf_overlay_interactive(errors, labels,
                                        title="Delivery-Time Models: |Error| ECDF",
                                        template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/comparison/error_ecdf_overlay_interactive.png" alt="error_ecdf_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
