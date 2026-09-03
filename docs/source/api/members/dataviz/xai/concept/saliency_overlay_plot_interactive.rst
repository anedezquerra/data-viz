dataviz.xai.concept.saliency_overlay_plot_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: saliency_overlay_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.concept import saliency_overlay_plot_interactive

   rng = np.random.default_rng(3)
   images = [rng.random((12, 12)) for _ in range(3)]
   saliencies = [rng.random((12, 12)) for _ in range(3)]
   labels = ["sample A", "sample B", "sample C"]

   fig = saliency_overlay_plot_interactive(images, saliencies, labels=labels)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
