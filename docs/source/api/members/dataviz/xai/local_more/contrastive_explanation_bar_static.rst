dataviz.xai.local_more.contrastive_explanation_bar_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: contrastive_explanation_bar_static

Use case
--------

Use to show why a prediction holds (pertinent positives) versus what minimal changes would flip it (pertinent negatives).

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.local_more import contrastive_explanation_bar_static

   pertinent_positives = {"income": 52.0, "tenure": 4.0}
   pertinent_negatives = {"debt": 8.0, "region_score": 0.3}

   ax = contrastive_explanation_bar_static(pertinent_positives, pertinent_negatives)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/contrastive_explanation_bar_static.png" alt="contrastive_explanation_bar_static example output"><figcaption>Example output</figcaption></figure></div>
