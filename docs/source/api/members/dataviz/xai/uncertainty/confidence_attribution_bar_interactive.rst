dataviz.xai.uncertainty.confidence_attribution_bar_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: confidence_attribution_bar_interactive

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

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
