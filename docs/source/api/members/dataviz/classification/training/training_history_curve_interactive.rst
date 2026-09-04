dataviz.classification.training.training_history_curve_interactive
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.training</p></div>

.. currentmodule:: dataviz.classification.training

.. autofunction:: training_history_curve_interactive

Use case
--------

Use to monitor fit quality over epochs; plots loss or metric series with validation curves dashed.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.training import training_history_curve_interactive

   # neural churn classifier: 40-epoch log-loss history
   epochs = np.arange(1, 41)
   loss = 0.9 * np.exp(-epochs / 9.0) + 0.32
   val_loss = 0.9 * np.exp(-epochs / 8.0) + 0.36 + np.maximum(epochs - 25, 0) * 0.004
   history = {"loss": loss.tolist(), "val_loss": val_loss.tolist()}

   fig = training_history_curve_interactive(history,
                                            title="Churn MLP: training history")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/training/training_history_curve_interactive.png" alt="training_history_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
