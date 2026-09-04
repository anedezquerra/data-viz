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

   scores = {
       "lung opacity": 0.88,
       "pleural effusion": 0.82,
       "cardiomegaly": 0.74,
       "rib fracture": 0.61,
       "medical device": 0.55,
       "text marker": 0.42,
   }
   p_values = {
       "lung opacity": 0.001,
       "pleural effusion": 0.004,
       "cardiomegaly": 0.012,
       "rib fracture": 0.03,
       "medical device": 0.08,
       "text marker": 0.21,
   }

   ax = concept_activation_bar_static(
       scores,
       p_values=p_values,
       significance=0.05,
       title="TCAV Concept Scores - Pneumonia X-Ray Classifier",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/concept/concept_activation_bar_static.png" alt="concept_activation_bar_static example output"><figcaption>Example output</figcaption></figure></div>
