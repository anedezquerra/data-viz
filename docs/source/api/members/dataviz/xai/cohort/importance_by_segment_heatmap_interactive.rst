dataviz.xai.cohort.importance_by_segment_heatmap_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.cohort</p></div>

.. currentmodule:: dataviz.xai.cohort

.. autofunction:: importance_by_segment_heatmap_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.cohort import importance_by_segment_heatmap_interactive

   importances = {
       "young": {"age": 0.30, "income": 0.12, "tenure": 0.08},
       "middle": {"age": 0.18, "income": 0.25, "tenure": 0.10},
       "senior": {"age": 0.10, "income": 0.20, "tenure": 0.22},
   }

   fig = importance_by_segment_heatmap_interactive(importances)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
