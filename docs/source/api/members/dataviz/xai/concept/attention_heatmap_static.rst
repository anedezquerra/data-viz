dataviz.xai.concept.attention_heatmap_static
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: attention_heatmap_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.concept import attention_heatmap_static

   rng = np.random.default_rng(5)
   attention = rng.random((4, 4))
   tokens_x = ["loan", "amount", "risk", "score"]

   ax = attention_heatmap_static(attention, tokens_x)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/concept/attention_heatmap_static.png" alt="attention_heatmap_static example output"><figcaption>Example output</figcaption></figure></div>
