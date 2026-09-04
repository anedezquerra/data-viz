dataviz.regression.validation.training_history_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: training_history_interactive

Use case
--------

Use to monitor training by plotting per-epoch metric curves such as loss and val_loss to spot divergence, plateaus, or overfitting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.validation import training_history_interactive

   rng = np.random.default_rng(42)
   epochs = np.arange(1, 21)
   train_rmse = 42 * np.exp(-epochs / 6.0) + 8.5 + rng.normal(0, 0.25, 20)
   val_rmse = 42 * np.exp(-epochs / 6.5) + 10.8 + rng.normal(0, 0.35, 20)
   val_rmse[14:] += np.linspace(0, 1.8, 6)  # onset of overfitting
   history = {"train_rmse": train_rmse, "val_rmse": val_rmse}

   fig = training_history_interactive(
       history,
       title="Demand forecasting MLP: training history (RMSE, k units)",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/training_history_interactive.png" alt="training_history_interactive example output"><figcaption>Example output</figcaption></figure></div>
