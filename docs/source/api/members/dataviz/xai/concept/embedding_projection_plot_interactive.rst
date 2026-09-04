dataviz.xai.concept.embedding_projection_plot_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: embedding_projection_plot_interactive

Use case
--------

Use to explore a 2-D embedding projection colored by class or feature value to spot clusters and outliers.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.concept import embedding_projection_plot_interactive

   rng = np.random.default_rng(9)
   coords = rng.normal(0.0, 1.0, size=(40, 2))
   labels = ["low" if v < 0 else "high" for v in coords[:, 0]]

   fig = embedding_projection_plot_interactive(coords, labels=labels)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/concept/embedding_projection_plot_interactive.png" alt="embedding_projection_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
