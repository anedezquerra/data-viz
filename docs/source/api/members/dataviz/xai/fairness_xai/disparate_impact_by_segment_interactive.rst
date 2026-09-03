dataviz.xai.fairness_xai.disparate_impact_by_segment_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.fairness_xai</p></div>

.. currentmodule:: dataviz.xai.fairness_xai

.. autofunction:: disparate_impact_by_segment_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.fairness_xai import disparate_impact_by_segment_interactive

   segment_metrics = pd.DataFrame(
       {"importance": [0.28, 0.22, 0.15], "positive_rate": [0.62, 0.55, 0.41]},
       index=["group_a", "group_b", "group_c"],
   )

   fig = disparate_impact_by_segment_interactive(segment_metrics, reference_rate=0.62)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
