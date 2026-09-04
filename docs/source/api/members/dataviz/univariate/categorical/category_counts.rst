dataviz.univariate.categorical.category_counts
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.categorical</p></div>

.. currentmodule:: dataviz.univariate.categorical

.. autofunction:: category_counts

Use case
--------

Use to compute sorted category counts or proportions, optionally limited to the top N, as input for categorical charts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.categorical import category_counts

   # Exit-survey responses for a public library membership program
   rng = np.random.default_rng(42)
   ratings = pd.Series(
       rng.choice(
           ["Excellent", "Good", "Average", "Poor"],
           size=180,
           p=[0.45, 0.32, 0.16, 0.07],
       ),
       name="rating",
   )

   result = category_counts(ratings, normalize=True, top_n=4)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
