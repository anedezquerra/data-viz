dataviz.xai.cohort.importance_by_segment_heatmap_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.cohort</p></div>

.. currentmodule:: dataviz.xai.cohort

.. autofunction:: importance_by_segment_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.cohort import importance_by_segment_heatmap_static

   importances = {
       "young": {"age": 0.30, "income": 0.12, "tenure": 0.08},
       "middle": {"age": 0.18, "income": 0.25, "tenure": 0.10},
       "senior": {"age": 0.10, "income": 0.20, "tenure": 0.22},
   }

   ax = importance_by_segment_heatmap_static(importances)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/cohort/importance_by_segment_heatmap_static.png" alt="importance_by_segment_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
