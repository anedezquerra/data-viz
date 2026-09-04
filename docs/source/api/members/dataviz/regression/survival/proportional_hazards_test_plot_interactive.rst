dataviz.regression.survival.proportional_hazards_test_plot_interactive
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.survival</p></div>

.. currentmodule:: dataviz.regression.survival

.. autofunction:: proportional_hazards_test_plot_interactive

Use case
--------

Use to check the Cox proportional-hazards assumption per covariate; bars below the alpha line flag Schoenfeld test violations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.regression.survival import proportional_hazards_test_plot_interactive

   covariates = ["age", "bmi", "smoker", "stage", "treatment", "sex"]
   p_values = [0.62, 0.31, 0.08, 0.012, 0.44, 0.71]

   fig = proportional_hazards_test_plot_interactive(
       covariates, p_values, alpha=0.05,
       title="Schoenfeld test of the proportional-hazards assumption",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/survival/proportional_hazards_test_plot_interactive.png" alt="proportional_hazards_test_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
