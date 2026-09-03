dataviz.xai.concept.concept_activation_bar_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: concept_activation_bar_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.concept import concept_activation_bar_interactive

   scores = {"striped": 0.62, "dotted": 0.35, "metallic": 0.12, "wooden": 0.48}
   p_values = {"striped": 0.001, "dotted": 0.04, "metallic": 0.30, "wooden": 0.008}

   fig = concept_activation_bar_interactive(scores, p_values=p_values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/xai/concept/concept_activation_bar_interactive.png" alt="concept_activation_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
