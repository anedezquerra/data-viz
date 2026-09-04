dataviz.regression.charts.prediction_plot
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.charts</p></div>

.. currentmodule:: dataviz.regression.charts

.. autofunction:: prediction_plot

Use case
--------

Use to compare observed versus predicted values; points off the diagonal reveal bias and where the model under- or over-predicts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.charts import prediction_plot

   rng = np.random.default_rng(42)
   n = 26
   actual = rng.uniform(120, 480, n)
   predicted = actual * rng.normal(1.0, 0.06, n)

   ax = prediction_plot(actual, predicted,
                        title="Insurance Claim Severity: Predicted vs Actual",
                        color="#1f6fb2", edgecolor="white")
   ax.set_xlabel("Actual claim cost (k USD)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/charts/prediction_plot.png" alt="prediction_plot example output"><figcaption>Example output</figcaption></figure></div>
