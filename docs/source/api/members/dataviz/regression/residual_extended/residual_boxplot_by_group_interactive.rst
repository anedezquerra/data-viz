dataviz.regression.residual_extended.residual_boxplot_by_group_interactive
==========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.residual_extended</p></div>

.. currentmodule:: dataviz.regression.residual_extended

.. autofunction:: residual_boxplot_by_group_interactive

Use case
--------

Use to compare residual spread and bias across categorical groups such as sites, cohorts, or segments.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.residual_extended import residual_boxplot_by_group_interactive

   rng = np.random.default_rng(42)
   n = 36
   shifts = pd.Series(np.repeat(["Day", "Swing", "Night"], 12), name="shift")
   actual_output = pd.Series(rng.normal(480, 45, n).round(0), name="actual_units")
   shift_bias = shifts.map({"Day": 4.0, "Swing": -2.0, "Night": -9.0})
   predicted_output = pd.Series(
       actual_output + shift_bias + rng.normal(0, 18, n), name="predicted_units"
   )

   fig = residual_boxplot_by_group_interactive(
       actual_output, predicted_output, shifts,
       title="Factory output model: residuals by shift",
       color="#4878d0", template="plotly_white",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/residual_extended/residual_boxplot_by_group_interactive.png" alt="residual_boxplot_by_group_interactive example output"><figcaption>Example output</figcaption></figure></div>
