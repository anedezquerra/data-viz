dataviz.regression.helpers.influence_statistics
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autofunction:: influence_statistics

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.helpers import influence_statistics

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(50, 3))
   y_true = rng.normal(10.0, 2.0, size=50)
   y_pred = y_true + rng.normal(0.0, 0.5, size=50)

   result = influence_statistics(X, y_true, y_pred)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
