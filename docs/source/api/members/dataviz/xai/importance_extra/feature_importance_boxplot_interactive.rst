dataviz.xai.importance_extra.feature_importance_boxplot_interactive
===================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: feature_importance_boxplot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.importance_extra import feature_importance_boxplot_interactive

   rng = np.random.default_rng(23)
   per_fold = {
       "age": rng.normal(0.05, 0.01, 5).tolist(),
       "income": rng.normal(0.12, 0.02, 5).tolist(),
       "tenure": rng.normal(0.02, 0.005, 5).tolist(),
   }

   fig = feature_importance_boxplot_interactive(per_fold)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
