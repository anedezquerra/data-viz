dataviz.regression.helpers.variance_inflation_factors
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autofunction:: variance_inflation_factors

Use case
--------

Use to compute one VIF per predictor column when screening a design matrix for multicollinearity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.helpers import variance_inflation_factors

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(50, 3))

   result = variance_inflation_factors(X)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
