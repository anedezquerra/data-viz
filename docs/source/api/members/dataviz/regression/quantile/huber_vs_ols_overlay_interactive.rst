dataviz.regression.quantile.huber_vs_ols_overlay_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.quantile</p></div>

.. currentmodule:: dataviz.regression.quantile

.. autofunction:: huber_vs_ols_overlay_interactive

Use case
--------

Use to show how a robust Huber fit diverges from OLS on data containing outliers.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.quantile import huber_vs_ols_overlay_interactive

   rng = np.random.default_rng(42)
   experience_yr = pd.Series(rng.uniform(0, 25, 24).round(1), name="experience_yr")
   salary_kusd = pd.Series(
       45 + 3.2 * experience_yr + rng.normal(0, 6, 24), name="salary_kusd"
   )
   salary_kusd.iloc[[3, 11]] += 55  # executive outliers
   ols_coef = np.polyfit(experience_yr, salary_kusd, 1)
   y_ols = pd.Series(np.polyval(ols_coef, experience_yr), name="ols_fit")
   weights = np.ones(24)
   for _ in range(8):
       resid = salary_kusd.to_numpy() - np.polyval(ols_coef, experience_yr)
       scale = max(1.345 * np.median(np.abs(resid)) / 0.6745, 1e-6)
       weights = np.minimum(1.0, scale / np.maximum(np.abs(resid), 1e-9))
       w_fit = np.polyfit(experience_yr, salary_kusd, 1, w=weights)
       ols_coef_huber = w_fit
   y_huber = pd.Series(np.polyval(ols_coef_huber, experience_yr), name="huber_fit")

   fig = huber_vs_ols_overlay_interactive(
       experience_yr, salary_kusd, y_ols, y_huber,
       title="Compensation study: Huber vs OLS with outliers",
       ols_color="#4878d0", huber_color="#d62728", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/quantile/huber_vs_ols_overlay_interactive.png" alt="huber_vs_ols_overlay_interactive example output"><figcaption>Example output</figcaption></figure></div>
