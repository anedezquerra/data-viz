dataviz.univariate.text.token_count_summary
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.text</p></div>

.. currentmodule:: dataviz.univariate.text

.. autofunction:: token_count_summary

Use case
--------

Use to profile text fields by whitespace token count, for example message or description verbosity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.text import token_count_summary

   rng = np.random.default_rng(42)
   vocab = ["battery", "screen", "delivery", "quality", "support", "price", "design", "fast"]
   reviews = pd.Series(
       [" ".join(rng.choice(vocab, size=rng.integers(3, 9))) for _ in range(60)],
       name="review",
   )
   result = token_count_summary(reviews)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
