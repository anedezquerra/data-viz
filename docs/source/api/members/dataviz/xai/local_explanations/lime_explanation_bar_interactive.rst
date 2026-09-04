dataviz.xai.local_explanations.lime_explanation_bar_interactive
===============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_explanations</p></div>

.. currentmodule:: dataviz.xai.local_explanations

.. autofunction:: lime_explanation_bar_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.local_explanations import lime_explanation_bar_interactive

   contributions = [
       ("income > 50k", 0.21),
       ("tenure <= 2", -0.13),
       ("debt > 10k", -0.08),
       ("age > 40", 0.05),
   ]

   fig = lime_explanation_bar_interactive(contributions)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_explanations/lime_explanation_bar_interactive.png" alt="lime_explanation_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
