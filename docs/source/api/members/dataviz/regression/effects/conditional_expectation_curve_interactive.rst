dataviz.regression.effects.conditional_expectation_curve_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: conditional_expectation_curve_interactive

Use case
--------

Use to plot E[Y|x] with an optional confidence band when summarizing the expected outcome as a smooth function of one predictor.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.effects import conditional_expectation_curve_interactive

   grid = pd.Series(np.linspace(18, 42, 24), name="bmi")
   ce = pd.Series(70 + 0.9 * (grid - 25) + 0.06 * (grid - 25) ** 2,
                  name="e_bp")
   lo = ce - 3.0
   hi = ce + 3.0

   fig = conditional_expectation_curve_interactive(
       grid, ce, ci_lower=lo, ci_upper=hi,
       title="E[Systolic BP | BMI] with 95% Band",
       feature_name="BMI", color="#c0392b", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/conditional_expectation_curve_interactive.png" alt="conditional_expectation_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
