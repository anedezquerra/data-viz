dataviz.regression.validation.cv_score_plot_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: cv_score_plot_interactive

Use case
--------

Use to judge model stability by inspecting per-fold cross-validation scores against their mean; high variance across folds warns of sensitivity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.regression.validation import cv_score_plot_interactive

   fold_r2 = [0.812, 0.795, 0.834, 0.807, 0.851, 0.788, 0.822, 0.815]

   fig = cv_score_plot_interactive(
       fold_r2, model_name="Gradient boosting (wine quality)",
       title="8-fold cross-validation R-squared",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/validation/cv_score_plot_interactive.png" alt="cv_score_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
