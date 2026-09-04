dataviz.univariate.ordinal.ordered_category_counts
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.ordinal</p></div>

.. currentmodule:: dataviz.univariate.ordinal

.. autofunction:: ordered_category_counts

Use case
--------

Use to count or normalize ordinal responses in a meaningful category order instead of frequency-sorted order.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.ordinal import ordered_category_counts

   rng = np.random.default_rng(42)
   scale = ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
   satisfaction = pd.Series(
       rng.choice(scale, size=220, p=[0.08, 0.17, 0.20, 0.35, 0.20]),
       name="satisfaction",
   )
   result = ordered_category_counts(satisfaction, order=scale, normalize=True)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
