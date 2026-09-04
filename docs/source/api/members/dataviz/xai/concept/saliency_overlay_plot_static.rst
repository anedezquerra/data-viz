dataviz.xai.concept.saliency_overlay_plot_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: saliency_overlay_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.concept import saliency_overlay_plot_static

   rng = np.random.default_rng(3)
   images = [rng.random((12, 12)) for _ in range(3)]
   saliencies = [rng.random((12, 12)) for _ in range(3)]
   labels = ["sample A", "sample B", "sample C"]

   ax = saliency_overlay_plot_static(images, saliencies, labels=labels)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/concept/saliency_overlay_plot_static.png" alt="saliency_overlay_plot_static example output"><figcaption>Example output</figcaption></figure></div>
