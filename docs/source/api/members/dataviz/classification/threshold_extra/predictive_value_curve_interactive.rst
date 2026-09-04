dataviz.classification.threshold_extra.predictive_value_curve_interactive
=========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold_extra</p></div>

.. currentmodule:: dataviz.classification.threshold_extra

.. autofunction:: predictive_value_curve_interactive

Use case
--------

Use to show how PPV and NPV shift with prevalence for a test of fixed sensitivity and specificity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold_extra import predictive_value_curve_interactive

   # fixed test characteristics: PPV collapses at low prevalence
   fig = predictive_value_curve_interactive(
       sensitivity=0.92, specificity=0.88,
       prevalences=np.linspace(0.001, 0.5, 150),
       title="Screening test: PPV / NPV vs prevalence")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold_extra/predictive_value_curve_interactive.png" alt="predictive_value_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
