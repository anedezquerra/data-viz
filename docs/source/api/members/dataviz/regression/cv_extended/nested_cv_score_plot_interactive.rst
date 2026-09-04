dataviz.regression.cv_extended.nested_cv_score_plot_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.cv_extended</p></div>

.. currentmodule:: dataviz.regression.cv_extended

.. autofunction:: nested_cv_score_plot_interactive

Use case
--------

Use to display outer-fold scores from nested CV, giving an unbiased estimate of performance after hyperparameter tuning.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.cv_extended import nested_cv_score_plot_interactive

   outer_folds = ["Fold 1", "Fold 2", "Fold 3", "Fold 4", "Fold 5"]
   scores = np.array([0.81, 0.77, 0.84, 0.79, 0.82])

   fig = nested_cv_score_plot_interactive(outer_folds, scores,
                                          title="Churn Value Model: Nested CV R2",
                                          metric_name="R2", color="#2a7f62",
                                          template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/cv_extended/nested_cv_score_plot_interactive.png" alt="nested_cv_score_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
