dataviz.xai.uncertainty.confidence_attribution_bar_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: confidence_attribution_bar_static

Use case
--------

Use to attribute predictive uncertainty to individual features, identifying which inputs drive the model's lack of confidence.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.uncertainty import confidence_attribution_bar_static

   attribution = {
       "entropy": 0.42,
       "margin": 0.31,
       "variance": 0.18,
       "disagreement": 0.09,
   }

   ax = confidence_attribution_bar_static(attribution)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/uncertainty/confidence_attribution_bar_static.png" alt="confidence_attribution_bar_static example output"><figcaption>Example output</figcaption></figure></div>
