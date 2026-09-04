dataviz.xai.concept.saliency_overlay_plot_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: saliency_overlay_plot_static

Use case
--------

Use to inspect which image regions drive a vision model by overlaying saliency or Grad-CAM heatmaps on the inputs.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.concept import saliency_overlay_plot_static

   rng = np.random.default_rng(42)
   size = 32
   yy, xx = np.mgrid[0:size, 0:size]
   centers = [(10, 12), (22, 9), (16, 20), (8, 24)]
   labels = ["Pneumonia", "Normal", "Effusion", "Mass"]

   images, saliencies = [], []
   for cx, cy in centers:
       blob = np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / 30.0)
       images.append(blob + rng.normal(0, 0.05, size=(size, size)))
       focus = np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / 18.0)
       saliencies.append(focus + rng.normal(0, 0.03, size=(size, size)))

   ax = saliency_overlay_plot_static(
       images,
       saliencies,
       labels=labels,
       title="Grad-CAM Overlays - Chest X-Ray Classifier",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/concept/saliency_overlay_plot_static.png" alt="saliency_overlay_plot_static example output"><figcaption>Example output</figcaption></figure></div>
