dataviz.classification.training.cv_score_boxplot_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.training</p></div>

.. currentmodule:: dataviz.classification.training

.. autofunction:: cv_score_boxplot_interactive

Use case
--------

Use to compare model candidates on cross-validation stability; one box per model over per-fold scores.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.training import cv_score_boxplot_interactive

   rng = np.random.default_rng(42)
   # 10-fold CV F1 scores for four churn model candidates
   cv_scores = {
       "logreg": rng.normal(0.72, 0.03, 10),
       "random forest": rng.normal(0.79, 0.025, 10),
       "gradient boost": rng.normal(0.81, 0.02, 10),
       "naive bayes": rng.normal(0.66, 0.04, 10),
   }

   fig = cv_score_boxplot_interactive(cv_scores,
                                      title="Churn models: 10-fold CV F1")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/training/cv_score_boxplot_interactive.png" alt="cv_score_boxplot_interactive example output"><figcaption>Example output</figcaption></figure></div>
