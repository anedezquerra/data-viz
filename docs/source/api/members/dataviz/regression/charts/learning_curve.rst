dataviz.regression.charts.learning_curve
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.charts</p></div>

.. currentmodule:: dataviz.regression.charts

.. autofunction:: learning_curve

Use case
--------

Use to see how model performance scales with training-set size and decide whether more data or a different model will help.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.charts import learning_curve

   train_sizes = np.array([20, 40, 60, 80, 100, 120])
   train_scores = np.array([0.99, 0.97, 0.96, 0.95, 0.945, 0.94])
   val_scores = np.array([0.62, 0.71, 0.77, 0.81, 0.83, 0.845])

   ax = learning_curve(train_sizes, train_scores, val_scores,
                       title="Yield Prediction: Learning Curve (R2)")
   ax.set_ylim(0.5, 1.02)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/charts/learning_curve.png" alt="learning_curve example output"><figcaption>Example output</figcaption></figure></div>
