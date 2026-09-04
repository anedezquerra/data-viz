dataviz.xai.uncertainty.confidence_attribution_bar_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: confidence_attribution_bar_interactive

Use case
--------

Use to attribute predictive uncertainty to individual features, identifying which inputs drive the model's lack of confidence.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.uncertainty import confidence_attribution_bar_interactive

   attribution = {
       "entropy": 0.42,
       "margin": 0.31,
       "variance": 0.18,
       "disagreement": 0.09,
   }

   fig = confidence_attribution_bar_interactive(attribution)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/uncertainty/confidence_attribution_bar_interactive.png" alt="confidence_attribution_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
