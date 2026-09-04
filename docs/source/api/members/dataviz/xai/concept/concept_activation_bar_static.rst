dataviz.xai.concept.concept_activation_bar_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: concept_activation_bar_static

Use case
--------

Use to test whether human-interpretable concepts influence a neural network, with non-significant concepts greyed out.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.concept import concept_activation_bar_static

   scores = {"striped": 0.62, "dotted": 0.35, "metallic": 0.12, "wooden": 0.48}
   p_values = {"striped": 0.001, "dotted": 0.04, "metallic": 0.30, "wooden": 0.008}

   ax = concept_activation_bar_static(scores, p_values=p_values)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/concept/concept_activation_bar_static.png" alt="concept_activation_bar_static example output"><figcaption>Example output</figcaption></figure></div>
