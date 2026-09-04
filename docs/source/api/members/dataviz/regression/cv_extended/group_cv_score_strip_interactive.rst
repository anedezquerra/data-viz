dataviz.regression.cv_extended.group_cv_score_strip_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.cv_extended</p></div>

.. currentmodule:: dataviz.regression.cv_extended

.. autofunction:: group_cv_score_strip_interactive

Use case
--------

Use to plot CV scores per group in grouped cross-validation, exposing groups where the model generalizes poorly.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.cv_extended import group_cv_score_strip_interactive

   plants = ["Plant A", "Plant B", "Plant C", "Plant D", "Plant E"]
   scores = np.array([0.72, 0.83, 0.68, 0.79, 0.75])

   fig = group_cv_score_strip_interactive(plants, scores,
                                          title="OEE Model: Leave-One-Plant-Out R2",
                                          metric_name="R2", color="#c0392b",
                                          template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/cv_extended/group_cv_score_strip_interactive.png" alt="group_cv_score_strip_interactive example output"><figcaption>Example output</figcaption></figure></div>
