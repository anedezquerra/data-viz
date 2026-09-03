dataviz.xai.local_explanations.lime_explanation_bar_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_explanations</p></div>

.. currentmodule:: dataviz.xai.local_explanations

.. autofunction:: lime_explanation_bar_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.local_explanations import lime_explanation_bar_static

   contributions = [
       ("income > 50k", 0.21),
       ("tenure <= 2", -0.13),
       ("debt > 10k", -0.08),
       ("age > 40", 0.05),
   ]

   ax = lime_explanation_bar_static(contributions)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
