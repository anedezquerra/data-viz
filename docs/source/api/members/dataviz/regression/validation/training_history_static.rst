dataviz.regression.validation.training_history_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: training_history_static

Use case
--------

Use to monitor training by plotting per-epoch metric curves such as loss and val_loss to spot divergence, plateaus, or overfitting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.validation import training_history_static

   rng = np.random.default_rng(42)
   epochs = np.arange(1, 21)
   train_rmse = 42 * np.exp(-epochs / 6.0) + 8.5 + rng.normal(0, 0.25, 20)
   val_rmse = 42 * np.exp(-epochs / 6.5) + 10.8 + rng.normal(0, 0.35, 20)
   val_rmse[14:] += np.linspace(0, 1.8, 6)  # onset of overfitting
   history = {"train_rmse": train_rmse, "val_rmse": val_rmse}

   ax = training_history_static(
       history,
       title="Demand forecasting MLP: training history (RMSE, k units)",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/training_history_static.png" alt="training_history_static example output"><figcaption>Example output</figcaption></figure></div>
