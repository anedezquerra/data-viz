dataviz.regression.gof.normality_test_panel_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.gof</p></div>

.. currentmodule:: dataviz.regression.gof

.. autofunction:: normality_test_panel_interactive

Use case
--------

Use to assess residual normality with a histogram, Q-Q plot, and Jarque-Bera annotation in one view.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.gof import normality_test_panel_interactive

   rng = np.random.default_rng(42)
   n = 40
   square_feet = rng.uniform(800.0, 4000.0, n)
   bedrooms = rng.integers(1, 6, n).astype(float)
   X = pd.DataFrame({"square_feet": square_feet, "bedrooms": bedrooms})
   price = 50.0 + 0.15 * square_feet + 12.0 * bedrooms
   residuals = pd.Series(rng.normal(0.0, 18.0, n), name="price_residuals_kusd")

   fig = normality_test_panel_interactive(
       residuals, title="Housing Price Model: Residual Normality",
       nbins=20, template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/gof/normality_test_panel_interactive.png" alt="normality_test_panel_interactive example output"><figcaption>Example output</figcaption></figure></div>
