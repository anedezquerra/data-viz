dataviz.univariate.text.top_terms
=================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.text</p></div>

.. currentmodule:: dataviz.univariate.text

.. autofunction:: top_terms

Use case
--------

Use to list the most frequent whitespace-delimited terms for lightweight text profiling without NLP dependencies.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.text import top_terms

   rng = np.random.default_rng(42)
   vocab = ["battery", "screen", "delivery", "quality", "support", "price", "design", "fast"]
   reviews = pd.Series(
       [" ".join(rng.choice(vocab, size=rng.integers(3, 9))) for _ in range(60)],
       name="review",
   )
   result = top_terms(reviews, top_n=8, lowercase=True)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
