dataviz.regression.learning.learning_curve_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.learning</p></div>

.. currentmodule:: dataviz.regression.learning

.. autofunction:: learning_curve_interactive

Use case
--------

Use to plot score against training-set size when diagnosing under- or overfitting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.learning import learning_curve_interactive

   rng = np.random.default_rng(42)
   train_sizes = np.array([20, 40, 60, 80, 100, 120, 150, 180])
   train_scores = pd.Series(0.99 - 0.10 * np.sqrt(train_sizes / 180.0)
                            + rng.normal(0, 0.005, 8), name="train_r2")
   val_scores = pd.Series(0.55 + 0.35 * (1.0 - np.exp(-train_sizes / 70.0))
                          + rng.normal(0, 0.01, 8), name="cv_r2")

   fig = learning_curve_interactive(train_sizes, train_scores, val_scores,
                                    title="Concrete Strength Model: Learning Curve",
                                    train_color="#1f77b4", val_color="#d62728",
                                    template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/learning/learning_curve_interactive.png" alt="learning_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
