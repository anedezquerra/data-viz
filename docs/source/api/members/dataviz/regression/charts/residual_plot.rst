dataviz.regression.charts.residual_plot
=======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.charts</p></div>

.. currentmodule:: dataviz.regression.charts

.. autofunction:: residual_plot

Use case
--------

Use as a first-pass diagnostic: residual patterns versus fitted values expose nonlinearity and heteroscedasticity before trusting inference.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.charts import residual_plot

   rng = np.random.default_rng(42)
   n = 26
   predicted = rng.uniform(30, 95, n)
   actual = predicted + rng.normal(0, 5, n) + 0.002 * (predicted - 60) ** 2

   ax = residual_plot(actual, predicted,
                      title="Compressor Efficiency Model: Residuals",
                      color="#2a7f62", edgecolor="white")
   ax.axhline(5.0, color="#888", linestyle=":", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/charts/residual_plot.png" alt="residual_plot example output"><figcaption>Example output</figcaption></figure></div>
