dataviz.classification.model_comparison.critical_difference_diagram_interactive
===============================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.model_comparison</p></div>

.. currentmodule:: dataviz.classification.model_comparison

.. autofunction:: critical_difference_diagram_interactive

Use case
--------

Use to compare classifiers across multiple datasets via average ranks and a critical-difference threshold.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.classification.model_comparison import (
       critical_difference_diagram_interactive,
   )

   rng = np.random.default_rng(73)
   # ranks of 4 models on 12 benchmark datasets (1 = best)
   rank_table = {
       "gbm": np.clip(rng.normal(1.8, 0.6, 12), 1, 4),
       "random forest": np.clip(rng.normal(2.2, 0.7, 12), 1, 4),
       "logreg": np.clip(rng.normal(3.0, 0.6, 12), 1, 4),
       "knn": np.clip(rng.normal(3.4, 0.5, 12), 1, 4),
   }

   fig = critical_difference_diagram_interactive(
       rank_table, cd=1.15,
       title="CD diagram: tabular benchmarks (Nemenyi, alpha=0.05)",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/model_comparison/critical_difference_diagram_interactive.png" alt="critical_difference_diagram_interactive example output"><figcaption>Example output</figcaption></figure></div>
