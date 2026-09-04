dataviz.univariate.transforms.transform_series
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.transforms</p></div>

.. currentmodule:: dataviz.univariate.transforms

.. autofunction:: transform_series

Use case
--------

Use to apply log, sqrt, Box-Cox, or Yeo-Johnson transformations to tame skew before analysis or modeling.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.transforms import transform_series

   rng = np.random.default_rng(42)
   reaction_ms = pd.Series(
       rng.gamma(shape=3.0, scale=90.0, size=150).round(1),
       name="reaction_ms",
   )
   result = transform_series(reaction_ms, method="sqrt")
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
