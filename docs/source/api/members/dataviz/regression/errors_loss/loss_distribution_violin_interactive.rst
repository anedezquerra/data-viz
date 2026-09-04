dataviz.regression.errors_loss.loss_distribution_violin_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.errors_loss</p></div>

.. currentmodule:: dataviz.regression.errors_loss

.. autofunction:: loss_distribution_violin_interactive

Use case
--------

Use to compare full per-observation loss distributions across models, catching heavy tails that mean error hides.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.errors_loss import loss_distribution_violin_interactive

   rng = np.random.default_rng(42)
   models = ["Ridge", "Random Forest", "XGBoost"]
   losses = [np.abs(rng.normal(0, 5, 30)),
             np.abs(rng.normal(0, 3.5, 30)),
             np.abs(rng.normal(0, 3.0, 30))]

   fig = loss_distribution_violin_interactive(
       models, losses,
       title="Freight Cost Models: Per-Shipment Absolute Loss",
       metric_name="absolute error (USD)", color="#1f6fb2",
       template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/errors_loss/loss_distribution_violin_interactive.png" alt="loss_distribution_violin_interactive example output"><figcaption>Example output</figcaption></figure></div>
