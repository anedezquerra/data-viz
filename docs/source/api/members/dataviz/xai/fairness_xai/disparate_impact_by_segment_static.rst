dataviz.xai.fairness_xai.disparate_impact_by_segment_static
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.fairness_xai</p></div>

.. currentmodule:: dataviz.xai.fairness_xai

.. autofunction:: disparate_impact_by_segment_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.xai.fairness_xai import disparate_impact_by_segment_static

   segment_metrics = pd.DataFrame(
       {"importance": [0.28, 0.22, 0.15], "positive_rate": [0.62, 0.55, 0.41]},
       index=["group_a", "group_b", "group_c"],
   )

   ax = disparate_impact_by_segment_static(segment_metrics, reference_rate=0.62)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/fairness_xai/disparate_impact_by_segment_static.png" alt="disparate_impact_by_segment_static example output"><figcaption>Example output</figcaption></figure></div>
